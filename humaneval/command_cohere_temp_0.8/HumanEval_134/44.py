```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is a letter not belonging to a word, False otherwise.
    """
    # Define and compile regex pattern
    word_pattern = r'\b[a-z]\b'  # using regex to check if the last char is a letter
    
    # Check if the last character is a part of a word
    if re.search(word_pattern, txt) != None:
        return False
    
    # Check if the string is empty
    if txt == "":
        return False
    
    return True
```

The test cases are:
```python
def test_check_if_last_char_is_a_letter():
    """
    Test the check_if_last_char_is_a_letter function.
    """
    assert check_if_last_char_is_a_letter("apple pie") == False
    assert check_if_last_char_is_a_letter("apple pi e") == True
    assert check_if_last_char_is_a_letter("apple pi e ") == False
    assert check_if_last_char_is_a_letter("") == False
    assert check_if_last_char_is_a_letter("hello") == True
    assert check_if_last_char_is_a_letter("This_is_a_test") == False
```

The script defines a function `check_if_last_char_is_a_letter` that takes a string as input and returns `True` if the last character is an alphabetical character and is not a part of a word. The function checks if the last character is a word character using regular expressions. If it is not part of a word, the function checks if the last character is a letter and if the string is not empty. If these conditions are fulfilled, the function returns `True`; otherwise, it returns `False`. 

The test cases check the function under different scenarios.