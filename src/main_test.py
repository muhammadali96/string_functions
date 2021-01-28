def capitalise_string(str):
    return str.upper()

def test_capitalise_string():
    assert capitalise_string("hello") == "HELLO"
    assert capitalise_string("hello world") == "HELLO WORLD"
    assert capitalise_string("today I am 25!") == "TODAY I AM 25!"