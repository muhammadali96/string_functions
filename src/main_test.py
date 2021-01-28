def capitalise_string(str):
    return str.upper()

def test_capitalise_string():
    assert capitalise_string("hello") == "HELLO"
    assert capitalise_string("hello world") == "HELLO WORLD"
    assert capitalise_string("today I am 25!") == "TODAY I AM 25!"

def decapitalise_string(str):
    return str.lower()

def test_decapitalise_string():
    assert decapitalise_string("HELLO") == "hello"
    assert decapitalise_string("HELLO WORLD") == "hello world"
    assert decapitalise_string("TODAY I AM 25!") == "today i am 25!"
