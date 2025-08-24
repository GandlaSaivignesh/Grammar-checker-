from flask import Flask, request, render_template_string
import webbrowser
import threading
import nltk
from nltk import word_tokenize, pos_tag

# Download NLTK resources if not already present
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

app = Flask(__name__)
# Grammar Functions
def get_pos(sentence):
    tokens = word_tokenize(sentence)
    return pos_tag(tokens)

def correct_sentence(tagged):
    words = [word for word, tag in tagged]
    corrected = words[:]

    if not words[0][0].isupper():
        corrected[0] = words[0].capitalize()

    for i in range(len(tagged) - 1):
        if tagged[i][1] == 'DT' and not tagged[i+1][1].startswith('NN'):
            corrected[i+1] = 'thing'
        if tagged[i][1].startswith('VB') and tagged[i+1][1].startswith('VB'):
            corrected[i+1] = 'it'
        if tagged[i][1] == 'NN' and tagged[i+1][1] == 'VB':
            verb = tagged[i+1][0]
            if verb.endswith('y') and verb[-2] not in "aeiou":
                corrected[i+1] = verb[:-1] + 'ies'
            elif verb.endswith(('s', 'sh', 'ch', 'x', 'z', 'o')):
                corrected[i+1] = verb + 'es'
            else:
                corrected[i+1] = verb + 's'

    return " ".join(corrected)

def check_grammar(tagged):
    errors = []
    for i in range(len(tagged) - 1):
        if tagged[i][1] == 'DT' and not tagged[i+1][1].startswith('NN'):
            errors.append(f"Determiner '{tagged[i][0]}' not followed by noun (found '{tagged[i+1][0]}')")
        if tagged[i][1].startswith('VB') and tagged[i+1][1].startswith('VB'):
            errors.append(f"Double verb '{tagged[i][0]} {tagged[i+1][0]}' detected")
        if tagged[i][1] == 'IN' and not (tagged[i+1][1].startswith('DT') or tagged[i+1][1].startswith('NN')):
            errors.append(f"Preposition '{tagged[i][0]}' not followed by noun/determiner (found '{tagged[i+1][0]}')")
        if tagged[i][1] == 'NN' and tagged[i+1][1] == 'VB':
            errors.append(f"Noun '{tagged[i][0]}' used with incorrect verb '{tagged[i+1][0]}'")
    if not tagged[0][0][0].isupper():
        errors.append("Sentence should start with a capital letter.")
    return errors

# Main route
@app.route('/', methods=['GET', 'POST'])
def index():
    sentence = ''
    tagged = []
    corrected = ''
    corrected_tagged = []
    errors = []

    try:
        if request.method == 'POST':
            sentence = request.form.get('sentence', '')
            tagged = get_pos(sentence)
            errors = check_grammar(tagged)
            if errors:
                corrected = correct_sentence(tagged)
                corrected_tagged = get_pos(corrected)
    except Exception as e:
        return f"<h2 style='color:red;'>⚠️ Error occurred: {e}</h2>"

    return render_template_string(html_template, sentence=sentence, tagged=tagged,
                                  corrected=corrected, corrected_tagged=corrected_tagged, errors=errors)

# Auto-open browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")
    from waitress import serve

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)
