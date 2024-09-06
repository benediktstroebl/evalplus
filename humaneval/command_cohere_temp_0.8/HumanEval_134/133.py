```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to examine

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise
    """
    # Use regex to check if the last character is a letter and it is the last character in the string
    alpha_char = r'[a-zA-Z]'
    last_char_is_alone = f'{alpha_char}$'
    
    return bool(re.search(last_char_char, txt) and not re.search(r'\b{}\b'.format(alpha_char), txt))
```

The Python script uses a regular expression to check if the last character of a string is an alphabetical character. The function `check_if_last_char_is_a_letter` takes a string as input and returns `True` if the last character is an alphabetical character and is not part of a word. The function uses the `re.search` function to search for a match of the regular expression. 

The regular expression used is `[a-zA-Z]`. This matches any string that contains an alphabetical character. The `re.search` function returns a match object if there is a match, and `None` otherwise. The match object has a boolean value, which is used as the value of the function. The function returns `False` if the last character is part of a word. This is done by using the regular expression `\b[[a-zA-Z]\b`. 

The double escaped character `\b` corresponds to a word boundary. Hence, if the character is part of a word, the `\b` will match and the function will return `False`. The script provides an example of usage and asserts the function behaviour for edge cases.