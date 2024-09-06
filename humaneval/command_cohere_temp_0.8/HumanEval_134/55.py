```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length to avoid runtime errors
    if len(txt)==0:
        return False
    # Use slicing to extract the last character and convert it to lowercase for case-insensitivity
    last_char = txt[-1].lower()
    # Use a boolean OR operation to check if the last character is a letter or digit
    if last_char in 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789':
        # Use a regex pattern to check if the last character is part of a word
        return not bool(re.match(r'[a-z]\w*,\s*[a-z]\w*', txt))
    return False
```

The function uses the last character extraction via slicing, converts it to lowercase to make the check case-insensitive, and evaluates it against the alphabet and digit characters using a boolean OR operation.

Further, a regex pattern is used to assess if the last character forms part of a word, avoiding false positives. The test cases assess the function's effectiveness against different scenarios.

You can test this function under other scenarios to further verify its correctness.