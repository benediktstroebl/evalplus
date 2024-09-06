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
            (not txt.split().endswith(last_char)))
```

The function uses the `isalpha()` method to check if the last character is an alphabetical character and the `endswith()` method to determine if the last character is part of a word. The function returns True if the last character is an alphabetical character and is not part of a word, and False otherwise. 

Here are examples of function calls with different input values:
```python
# These examples are taken from the provided test cases
assert check_if_last_char_is_a_letter("apple pie") == False
assert check_if_last_char_is_a_letter("apple pi e") == True
assert check_if_last_char_is_a_letter("apple pi e ") == False
assert check_if_last_char_is_a_letter("") == False 
```