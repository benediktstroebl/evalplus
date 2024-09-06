```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define a string literal representing space (" "):
    SPACE = " "

    # Check if the input string is empty:
    if not txt:
        return False

    # Split the string into words using split() method:
    words = txt.split(SPACE)
    # Get the last character:
    last_char = words[-1][-1] if len(words[-1]) > 0 else ""

    # Check if the last character is a letter and is not part of a word:
    return str.isalpha(last_char) and last_char != words[-1]
```

The provided solution uses the `split()` method to split the input string into words using space as a separator. Then, it extracts the last character and checks if it's an alphabetical character using the `str.isalpha()` method. Additionally, it verifies if the last character is not part of a word by checking if it's different from the last word in the split string. The function returns `True` if these conditions are met, and `False` otherwise.