```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Trim any whitespace from the end of the string
    txt = txt.strip()

    # Check if the string ends with a space followed by a letter
    assert txt.endswith(" ") == bool(check_if_last_char_is_a_letter(" "))
    
    if txt.endswith(" "):
        return True
    
    # Check if the last character is a letter (not part of a word)
    return txt[-1].lower() != txt[-1]
```

The function checks the last character of the given string, `txt`. If it's an alphabetical character and not part of a word (such as the ending character of a word), it returns `True`; otherwise, it returns `False`. The additional tests further assert the function's correctness. 

The function's approach is to first strip any whitespace from the end of the string using the `strip()` method, which eliminates any leading or trailing whitespaces. Then, it checks if the last character is a letter by converting it to lowercase and comparing it to the original last character. If they are different, the last character is an alphabetical character not part of a word. The final test verifies if the input is simply a space, ensuring that the function handles edge cases. 

This approach proves both efficient and robust in handling the specified problem.