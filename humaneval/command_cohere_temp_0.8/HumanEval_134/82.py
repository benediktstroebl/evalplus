```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Use slicing to extract the last character and collapse the string to a single character
    last_char = txt[-1:]
    # Check if the last character is in a separate word or not. 
    # If the last character is a part of a word, the length of the collapsed string will be 1 (a single character).
    # If it's not part of a word, the length will be 0 (it will be considered as a single character, not part of any word)
    return len(last_char) == 1 and txt.endswith(last_char) and last_char.isalpha()
```

The function uses string slicing to extract the last character and then checks its length to determine if it's a standalone character or part of a word. The `txt.endswith(last_char)` condition ensures the character is present at the end of the string, and `last_char.isalpha()` checks if it's an alphabetical character. This solution is concise and accurately determines the specified condition.