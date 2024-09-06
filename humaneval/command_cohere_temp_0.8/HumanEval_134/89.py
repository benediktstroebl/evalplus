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
    
    # Define the word boundary regex pattern
    word_boundry = r'\s'

    # Use regex to check if the last character is part of a word or not
    return not bool(re.search(f'(?<!\W){txt[-1]}{word_boundry}', txt))
```

This function uses a regular expression pattern `r'\s` to check if the last character is followed by a word boundary `(^\W|\b)`, indicating that it is not part of a word. The function returns `True` if the last character is an alphabetical character and is not part of a word, and `False` otherwise. You can use this function by passing in a string as an input like this: `print(check_if_last_char_is_a_letter("apple pi e"))`, and it should return `True`. 

*Note*: The specification of the problem does not specify the case sensitivity of the alphabetical character, so this function is case-sensitive due to the [default behavior of the Python regex library](https://docs.python.org/3/library/re.html#regex-patterns). If you want to make it case-insensitive, you have to update the regex pattern accordingly, e.g.: `r'[a-z]\b'` or `r'[A-Z]\b'`.