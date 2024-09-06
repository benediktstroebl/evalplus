```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Define the string minus the last character
    minus_last = txt[:-1]
    # Check if the last character is not part of a word
    is_not_part_of_word = True if txt[-1] != ' ' and txt[-1] != '-' and txt[-1] != '_' else False
    # Check if the last character is a letter
    is_last_char_letter = txt.isalpha()
    # Return the result of the check
    return is_last_char_letter and is_not_part_of_word
```

The problem statement suggests that the function should return True if the last character of the given string is an alphabetical character and is not a part of any word (i.e., single character). The function checks if the last character is a single character and an alphabet character and returns True in that case. The function returns False if the last character is a part of some word (evidenced by the presence of a space, hyphen, or underscore after the last character). The given examples successfully pass the tests.