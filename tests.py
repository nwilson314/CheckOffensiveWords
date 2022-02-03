from check_offensive_words import OffensiveWordChecker

def setup():
    owc = OffensiveWordChecker()

    return owc

def test_get_api_request_returns_dict_for_real_word():
    owc = setup()

    assert type(owc.get_api_request_json('hello')) == type(dict())

def test_get_api_request_returns_empty_dict_for_non_word():
    owc = setup()

    assert owc.get_api_request_json('`') == dict()

def test_run_word_returns_false_for_non_offensive_word():
    owc = setup()

    assert owc.run_word('hello') == False

def test_run_word_returns_false_for_non_word():
    owc = setup()

    assert owc.run_word('asdfadf') == False

def test_run_word_returns_true_for_offensive_word():
    owc = setup()

    assert owc.run_word('shit') == True

