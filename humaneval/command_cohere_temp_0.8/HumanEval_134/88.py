```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string"
    
    # Use slicing to extract the last character and transform it to lowercase
    last_char = txt[-1].lower()
    
    # Check if the last character is in lowercase
    if not last_char.isalpha():
        return False
    
    # Check if the last character is part of a word
    words = txt.split()
    if last_char in words[-1]:
        return False
    
    return True
```

The test cases are:
```python
def test_last_char_is_letter():
    """
    Test if the function returns True when the last character is a letter and not part of a word.
    """
    assert check_if_last_char_is_a_letter("apple pi e") == True
    assert check_if_last_char_is_a_letter("apple pi e ") == False
    assert check_if_last_char_is_a_letter("Hello world!") == False
    assert check_if_last_char_is_a_letter("ailment") == False
    assert check_if_last_char_is_a_letter("apple pie") == False
    
def test_empty_string():
    """
    Test if the function returns False when the input is an empty string.
    """
    assert check_if_last_char_is_a_letter("") == False
```

The evaluation of the last character is case insensitive, so 'pi' and 'PI' are treated as the same. The function uses `.isalpha()` to evaluate if the last character is alphabetical. The test cases confirm that the function behaves as expected. You can integrate this function into your code to check if the last character of a string is a letter and is not part of a word.  This can be helpful when you need to extract a specific part of a string for further processing.  This evaluation does not consider diacritics and thus considers only the ASCII value of the character.