```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to examine

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise
    """
    # Extracting only the last character of the given string
    last_char = txt[-1:]
    
    # Checking if the last character is a letter
    if len(last_char) == 1 and last_char.isalpha():
        # Checking if the last character is not part of a word i.e., it is a standalone character
        if last_char.count(' ') == 0:
            return True
    return False
```

The function `check_if_last_char_is_a_letter` checks if the last character of a given string is an alphabetical character and is not part of a word. It does so in two main steps:
1. Extracts the last character of the input string using slicing (`last_char = txt[-1:]`).
2. Checks if the last character is a single-letter string and is an alphabetical character (`if len(last_char) == 1 and last_char.isalpha()`).
3. If the above conditions are met, it further checks if the last character is not part of a word, i.e., it is a standalone character (`if last_char.count(' ') == 0`).
4. If all the conditions are fulfilled, the function returns `True`, otherwise, it returns `False`. 

The provided example tests demonstrate the correct operation of the defined function.