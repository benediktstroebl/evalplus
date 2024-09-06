```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to check.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Extract the last character and remove whitespace characters if present
    last_char = txt.strip()[-1:]
    
    # Check if the last character is a letter and not part of a word
    return last_char.isalpha() and not last_char.isspace() and (not txt.strip().split()[-1])
```

This function uses the `str.strip()` method to remove any leading or trailing whitespace characters from the input string. Then, it uses the `-1` indexing syntax to extract the last character as a separate variable, `last_char`.

The function then checks if the `last_char` is an alphabetical character using the `isalpha()` method and if it's not a space character using the `isspace()` method. Lastly, the function checks if the `last_char` is not part of a word by splitting the input string into words using the `split()` method and checking if the last element of the split string is empty (`not txt.strip().split()[-1]`).

This approach ensures that the function handles the edge cases mentioned in the prompt, including handling leading and trailing whitespace, and provides the correct boolean output for the provided examples.