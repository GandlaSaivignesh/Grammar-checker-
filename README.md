Objective

The project is a web-based Grammar Checker application that helps users identify and correct basic grammatical mistakes in English sentences. It uses Natural Language Processing (NLP) techniques to analyze text and provide corrections.

🔹 Key Features

Web Interface

Built using Flask (Python web framework).

User-friendly form where a sentence can be entered and checked.

NLP for Grammar Checking

Uses NLTK (Natural Language Toolkit) for tokenization and Part-of-Speech (POS) tagging.

Identifies grammatical structures like nouns, verbs, determiners, and prepositions.

Error Detection
The system checks for:

Missing capitalization at the start of a sentence.

A determiner (DT) not followed by a noun.

Double verbs used together.

Preposition (IN) not followed by noun/determiner.

Noun + incorrect verb form mismatch.

Error Correction

Capitalizes the first word of the sentence if needed.

Replaces incorrect structures with more appropriate words (e.g., "a is" → "a thing is").

Adjusts verb forms (e.g., "boy play" → "boy plays").

Interactive Output

Shows original sentence with POS tags.

Lists grammar errors found.

Displays corrected version of the sentence along with corrected POS tags.

🔹 Technologies Used

Python – Core programming language.

Flask – For creating the web interface.

NLTK – For tokenization and POS tagging.

HTML/CSS (via render_template_string) – For UI design.

Threading & Webbrowser – To auto-launch the app in the browser.

🔹 Workflow

User enters a sentence in the web form.

Sentence is tokenized and POS-tagged using NLTK.

Grammar rules are checked (e.g., determiners followed by nouns).

Errors are displayed if found, along with corrections.

Corrected sentence and POS tags are shown to the user.

If no errors → message: ✅ No grammatical errors found!
