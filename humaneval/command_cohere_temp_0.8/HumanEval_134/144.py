```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string to words and chech last char is not part of a word
    # If string is empty, return False
    if not txt:
        return False
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_char_is_letter = txt[-1] in letters
    return not last_char_is_letter and txt.split() != ['']
```

The function checks if the last character of a given string is an alphabetical character and is not part of a word. To do this, it first checks if the string is empty, and if so, it returns False. Then, it checks if the last character is part of a word or not, and if so, it returns False. If the last character is not part of a word, it checks if this character is an alphabetical character, and if so, it returns True. If the last character is not an alphabetical character, it returns False. 

You can test this function by calling it with different strings and verifying that it returns the expected results based on the provided problem statement.