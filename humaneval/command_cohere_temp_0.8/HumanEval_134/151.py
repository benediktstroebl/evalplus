```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.

    Examples:
    >>> check_if_last_char_is_a_letter("apple pie")
    False
    >>> check_if_last_char_is_a_letter("apple pi e")
    True
    >>> check_if_last_char_is_a_letter("apple pi e ")
    False
    >>> check_if_last_char_is_a_letter("")
    False
    """
    def is_alphabetical(char):
        return char.isalpha()

    def is_not_word(char):
        return char.isspace() or (char.isalpha() and char == txt[-1])

    return is_not_alphabetical(txt) and is_alphabetical(txt)
```

The function utilizes two auxiliary functions: `is_alphabetical` checks whether a given character is an alphabetical character, and `is_not_word` checks whether the given character is a space or is an alphabetical character and it's the same as the last character in the input string. Ultimately, the function returns `True` if the last character is an alphabetical character and is not part of a word, and `False` otherwise.