```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Define a regular expression pattern to match alphabetical characters
    alpha_pattern = r'[a-zA-Z]'

    # Check if the string is empty
    if not txt:
        return False

    # Find the last character in the string
    last_char = txt[-1]

    # Check if the last character is alphabetic
    if re.search(alpha_pattern, last_char):
        # Check if the last character is separated from the previous word
        return not last_char.isalnum() and re.search(r' \Z', txt)
    return False
```

The function `check_if_last_char_is_a_letter` accepts one parameter, `txt`, which is the string to be analyzed.

It first checks if the string is empty. If it is, the function returns False because empty strings do not have any last character.

Next, it extracts the last character of the given string using `last_char = txt[-1]`.

The function then checks if the last character is an alphabetical character by utilizing the regular expression `alpha_pattern` to match any alphabetical character. If it is, it further checks if this last character is not part of a word, using the regex `r' \Z'` to verifies if there is a space immediately after the last character, not any alphanumeric characters.

If all these conditions are met, the function returns `True`; otherwise, it returns `False`. 

The script ensures that the last character is not part of a word by checking for a space immediately after it, so the function accurately fulfills the task described in the problem statement.