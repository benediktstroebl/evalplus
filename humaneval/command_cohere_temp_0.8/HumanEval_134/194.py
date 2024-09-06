```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Trim any whitespace from the end of the string
    txt = txt.rstrip()
    # Check if the string ends with a space
    if txt.endswith(" "):
        return False
    # Check if the last character is a letter and not the last character of a word
    return txt[-1].isalpha() and not txt.endswith(txt[-1])
```

The function checks if the last character of the given string `txt` is an alphabetical character and is not part of a word. The Python built-in function `isalpha()` is used to check if the character is an alphabetical character, and the condition `not txt.endswith(txt[-1])` is used to verify if the character is the last character of a word or not. The function returns True if the conditions are met, and False otherwise.