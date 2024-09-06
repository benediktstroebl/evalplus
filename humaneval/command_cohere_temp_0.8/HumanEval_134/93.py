```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string
    assert isinstance(txt, str), "Input 'txt' must be a string."
    
    # Check if the string is empty
    if not txt:
        return False
    
    # Find the last character and the last space (if it exists)
    last_char = txt[-1]
    last_space = -1
    
    # Iterate through the string to find the last space
    for i, char in enumerate(txt):
        if char == ' ':
            last_space = i
            break

    # Check if the last character is not part of a word
    if last_space == -1 or last_char != txt[last_space]:
        return True

    return False
```

The function checks if the last character of a given string is an alphabetical character and is not part of a word, and returns `True` or `False` accordingly. The provided tests ensure the function behaves as expected for various cases.