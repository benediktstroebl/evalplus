```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Split the string into words using whitespace characters as separators
    words = txt.split()
    # If the string is empty or there are no words at all, return False
    if not txt or not words:
        return False
    # Reduce the list of words to only the last character of the last word
    last_char = words[-1][-1]
    # Check if the last character is in uppercase or lowercase alphabet
    if last_char in alphabetic:
        # Check if the last character is not part of a word (i.e., it's a lone character)
        return not words[-1].startswith(last_char)
    return False
```

The function `check_if_last_char_is_a_letter` uses string partitioning and list slicing techniques to extract the final character of the input string. Subsequently, it examines whether this character is from the alphabet and isn't a constituent of any word. Ultimately, it returns True if these conditions are met; otherwise, it returns False.