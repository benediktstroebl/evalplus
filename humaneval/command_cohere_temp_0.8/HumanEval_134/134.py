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
    txt = txt.strip()  # Remove leading/trailing spaces
    last_char = txt[-1]  # Get the last character

    # Determine if the last character is a letter and not part of a word
    return (last_char.isalpha() and 
            (not txt.split().isalnum() or last_char != txt.split()[-1]))
```

The function `check_if_last_char_is_a_letter` achieves the task by:
1. Removing any leading or trailing whitespaces using the `strip()` method.
2. Retrieving the last character of the cleaned string using indexing `-1` on the string.
3. Using the `isalpha()` method to check if the last character is an alphabetical character.
4. Analyzing if the last character is part of a "word" using the `split()` method, which splits the string into individual words.
5. The function returns `True` if the last character is an alphabetical character and is not part of a "word," and `False` otherwise.

The logic ensures accurate determination of whether the last character meets the specified conditions.