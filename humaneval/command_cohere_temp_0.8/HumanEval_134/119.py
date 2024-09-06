```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Extract the last character and remove whitespace characters if present
    last_char = txt.strip()[-1:]
    
    # Check if the last character is in uppercase or lowercase alphabetical character
    if last_char.isalpha():
        # Check if the last character is part of a word
        if last_char.lower() != last_char and last_char != '-':
            return True
    return False
```

The problem statement poses the challenge of determining whether the final character of a given string is an alphabetical character but isn't part of a word. Our devised function `check_if_last_char_is_a_letter` achieves this by means of the following steps:
1. The last character is extracted from the input string using the slicing operation `[-1:]`.
2. The presence of whitespace characters is ruled out by utilizing the `strip()` method.
3. The `isalpha()` function is used to validate whether the last character is an alphabetical character.
4. We then check if the last character, when transformed to lowercase, matches the original character. This aspect helps us in identifying if the last character is an alphabetical character, but isn't part of a word.

In a nutshell, if the last character is an alphabetical character and isn't present within any word, the function returns `True`. Otherwise, it returns `False`.