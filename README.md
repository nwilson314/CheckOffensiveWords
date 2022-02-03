# Offensive Word Checker
A simple application to test whether a word is offensive or not. Uses the [API from Merriam Webster](https://dictionaryapi.com/).

## To run
First, create a Python virtual environment at top level:
```
python3 -m venv ./env
```

Activate virtual environment and download requirements:
```
source ./env/bin/activate
pip install -r requirements.txt
```

Run the program in Interactive/REPL mode:
```
python3 check_offensive_words.py
```

Run the program in batch mode with a text file of words to be checked against:
```
python3 check_offensive_words.py <path_to_text_file>
```

The results will be printed to the screen in both cases.

## To test
Tests can be run with pytest by using the command:
```
pytest tests.py
```