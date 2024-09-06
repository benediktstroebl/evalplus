```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is a letter not part of a word, False otherwise.
    """
    # Define a variable to store the last character of the string
    last_char = txt[-1]

    # Check if the last character is a letter and not a space
    if last_char.isalpha() and (last_char != " "):
        # Check if the last character is part of a word or not
        if last_char.lower() != txt.split()[-1]:
            return True
    return False
```

The function `check_if_last_char_is_a_letter()` uses the string's last character as an argument. It initially verifies if the last character is an alphabetical character and is not a space using the `isalpha()` and `!= " "` conditions. When these criteria are fulfilled, it checks whether the last character belongs to a word or not by comparing its lowercase version with the capitalized word from which it is situated. A return statement with a Boolean value of True follows if the criteria are satisfied. If none of the above requirements are met, the function returns False. 

This solution is implemented in a way that is both efficient and easy to understand, making good use of Python's string manipulation features.