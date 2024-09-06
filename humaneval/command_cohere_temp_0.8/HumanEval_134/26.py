```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Define a variable to store the last character of the string
    last_char = txt[-1] if len(txt) > 0 else None

    # Check if the last character is a letter and not the last character of a word
    return (last_char.isalpha() and 
            (not txt.rsplit(' ', 1)[-1] == last_char or not txt.split(' ')[-1] == last_char))
```