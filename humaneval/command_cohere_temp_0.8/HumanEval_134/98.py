```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is a letter not belonging to a word, False otherwise.
    """
    # Ensure the input is a string
    if not isinstance(txt, str):
        raise TypeError("Input should be a string")

    # Split the string into words, excluding the last character
    words = txt.split()

    # Check if the string is empty
    if not words:
        return False

    # Check if the last character belongs to the last word
    last_char = words[-1][-1]
    if not (last_char.isalpha() and last_char != words[-1][-2]):
        return False

    # Check if the last character is standalone, i.e., not part of a word
    if not any(char.isspace() for char in words[-1] if char < last_char):
        return True

    return False
```

The function leverages Python's string manipulation features and the `isalpha()` method to determine if the last character is an alphabetical character. Additionally, it checks if the last character belongs to the utmost word and is not preceded by a space character, ensuring it isn't part of a word. Ultimately, it returns `True` if these conditions are met, and `False` otherwise. 

This approach allows the function to efficiently determine whether the last character of a given string is an alphabetical character and not part of a word.