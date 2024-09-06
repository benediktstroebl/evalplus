```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to be evaluated.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string length to grab the last character
    len_txt = len(txt) - 1;
    # Check if the string length is not zero to prevent an IndexError
    if len_txt > 0:
        # Check if the last character is a letter and is not part of a word
        if txt[len_txt] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and txt[-1] != '_':
            return True
    return False
```

The function `check_if_last_char_is_a_letter` takes a single argument `s`, which is the string text to be evaluated. It checks if the last character of the string is an alphabetical character and is not part of a word (i.e., is an orphan letter).

The function first retrieves the length of the passed string and reduces it by one to extract the last character. Next, it evaluates if the last character is a letter and denies the function if it is an underscore. The function returns `True` if all the conditions are met; otherwise, it returns `False`. 

This solution utilizes only native Python capabilities, solely relying on the intrinsic Python string and numeric functions. 

Note: This solution assumes that the last character of the input string is eligible for consideration, irrespective of its position in the string. Also, it assumes that the string may contain spaces, and each space separates a "word" in the string. If the string does not contain spaces, the last character is considered as part of a word if it is adjacent to another character (e.g., "applepie" -> False).  If you have a specific scenario in mind, please clarify the criteria for a "word," and I'll be glad to tailor the function accordingly.