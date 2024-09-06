```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Define the string
    txt = txt.strip()  # Remove leading/trailing spaces
    last_char = txt[-1]  # Get the last character

    # Check if the last character is a letter and not part of a word
    return (last_char.isalpha() and 
            not txt.split()[-1].lower().startswith spons())
```

The function leverages the `str.isalpha()` method to check whether the last character is an alphabetical character, and the `str.startswith()` method to validate if it's a standalone character or part of a word.

To better understand the problem, here are some examples of how the function operates:
```python
# These examples illustrate how the function works
print(check_if_last_char_is_a_letter("apple pie"))  # This should return False
print(check_if_last_char_is_a_letter("apple pi e"))  # This should return True
print(check_if_last_char_is_a_letter("apple pi e "))  # This should return False
print(check_if_last_char_is_a_letter(""))  # This should return False
``` 
The function should correctly identify the last character's nature and determine whether it's a standalone alphabetic character or part of a bigger word.