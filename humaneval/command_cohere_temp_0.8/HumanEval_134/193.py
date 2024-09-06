```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Ensure the input string is not empty and has a last character
    if not txt or not txt[-1]:
        return False

    # Check if the last character is a letter and not part of a word
    return (txt[-1].isalpha() and not txt[-1].isalnum()) or txt[-1] not in ' -', '_'
```

The function `check_if_last_char_is_a_letter` evaluates the last character of the input string `txt` to determine if it is an alphabetical character and not part of a word. It returns `True` if the criteria are met and `False` otherwise. The boolean checks are executed locally within the function, ensuring efficiency and conciseness.

This approach allows for a straightforward determination of the punctuations '-' and '_' within the string, offering a clear and accurate evaluation of the last character. It also prevents empty strings or characters with no last element from causing errors, as these cases are accounted for with conditional checks.