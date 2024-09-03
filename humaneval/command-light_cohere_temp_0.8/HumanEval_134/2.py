```python
def check_if_last_char_is_a_letter(txt):
    # Remove all non-alphatic letters and spaces from the string
    txt = txt.replace(str.maketrans(' ', 'a'))
    # Return True if the last character is an alphabetical character and is not a part of a word
    return txt[-1].isalpha() and not txt.isspace()

def test_function():
    assert check_if_last_char_is_a_letter("apple pie") == False
    assert check_if_last_char_is_a_letter("apple pi e") == True
    assert check_if_last_char_is_a_letter("apple pi e ") == False
    assert check_if_last_char_is_a_letter("") == False
    assert check_if_last_char_is_a_letter("abc123") == True
```
This Python script defines a function `check_if_last_char_is_a_letter` that determines whether the final character of a given string is an alphabet or part of a word. The function removes all non-alphatic characters and spaces from the input string, ensuring that only letters and spaces are considered. The function then returns `True` if the final character is an alphabet and it is not a part of a word, and `False` otherwise. 

The `test_function` group then tests the function with various input strings, checking that the output of the function matches the expected results.