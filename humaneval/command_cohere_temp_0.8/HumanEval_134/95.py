```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Trim any whitespace from the end of the string
    txt = txt.strip()
    # Check if the string is empty
    if not txt:
        return False
    # Check if the last character is a letter and not the last character of a word
    return txt[-1].isalpha() and not txt.rsplit(' ', 1)[-1].isalpha()
```

The function `check_if_last_char_is_a_letter` uses the `strip()` method to remove any whitespace at the end of the input string, which ensures consistent behavior across different examples. It then checks if the string is empty, which would imply that the last character is not a letter, and returns False in such cases.

Next, it checks if the last character of the string is an alphabetical character using the `isalpha()` method. If it is, it further checks whether this last character is not the last character of a word using the `rsplit(' ')` method, which splits the string at the first space after the last character. If the split returns only one element (`[][-1]`), meaning that there was no word boundary, then the last character is not part of a word.

The returned boolean value indicates whether the last character is an alphabetical character and is not part of a word, based on the provided test cases.