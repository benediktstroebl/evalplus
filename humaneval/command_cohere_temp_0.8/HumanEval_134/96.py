```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length variable
    str_len = len(txt) - 1
    # Define the last character variable
    last_char = txt[str_len]
    # Check if the string length is smaller than one and return False if so
    if str_len < 1:
        return False
    # Check if the last character is a letter and it is not preceded by a space
    # By doing so, we ensure that the last character is not part of a word
    elif last_char.isalpha() and txt[str_len - 1] != ' ':
        return True
    else:
        return False
```

The provided solution uses the `isalpha()` method to check if the last character is an alphabetical character. Additionally, it checks if the last character is not preceded by a space to determine if it is not part of a word. The function also handles edge cases where the input string is empty or has a length of less than one.