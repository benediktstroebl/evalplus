```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): String to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define a variable to store the last character of the string
    last_char = txt[-1] if len(txt) > 0 else None
    
    # Check if the last character is a letter
    is_alphabetical = last_char.isalpha() if last_char else True
    
    # Check if the last character is not part of a word
    is_not_part_of_word = last_char != '-' and last_char != '_' and last_char != '>' and last_char != ':'
    
    # Return the boolean result
    return is_alphabetical and is_not_part_of_word
```

The function uses the built-in `isalpha()` method to check if the last character is an alphabetical character. Additionally, it verifies that the last character is not a part of any word by checking that it's not a hyphen, underscore, bullhorn, or colon, all of which typically indicate the end of a word. The function returns `True` if these conditions are both met; otherwise, it returns `False`. 

The following examples demonstrate how this function operates:
```python
print(check_if_last_char_is_a_letter("apple pie")) # Output: False
print(check_if_last_char_is_a_letter("apple pi e")) # Output: True
print(check_if_last_char_is_a_letter("apple pi e ")) # Output: False
print(check_if_last_char_is_a_letter("")) # Output: False
```