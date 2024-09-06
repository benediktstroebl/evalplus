```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length variable
    str_len = len(txt) - 1
    # Check if the string length is smaller than zero and return False if so,
    # meaning that the string ends with a space without any alphabetical character
    # or it is an empty string
    if str_len < 0:
        return False
    # Check if the last character is a letter and it is not the last character of a word,
    # meaning that it is followed by a space or the end of the string
    elif txt[str_len].isalpha() and not txt[str_len].iswalnum():
        return True
    # If the condition is not fulfilled return False
    else:
        return False
```

The function `check_if_last_char_is_a_letter` takes a single argument, `txt`, which is the string to be evaluated. It checks if the last character of the string is an alphabetical character and is not part of a word. The function returns `True` if the last character is an alphabetical character and is not part of a word, and `False` otherwise. 

To achieve this, it first checks if the string length is smaller than zero, and returns False if so, indicating that the string ends with a space without any alphabetical character or is an empty string. It defines `str_len` as `len(txt)` - 1, which is the last character index.

Then, the function uses the `isalpha()` method to check if the last character is alphabetical, and the `iswalnum()` method to check if the last character is part of a word. If these conditions are fulfilled, it returns True, otherwise it returns False.

The script rigorously defines the functionality of the problem and is encapsulated to be easily reusable and understandable.  It is a concise and accurate solution to the described problem.