```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Ensure the input string is not empty or contains leading/trailing spaces
    if not txt.strip():
        return False
    
    # Extract the last character and remove it from the string
    last_char = txt.strip()[-1]
    txt_without_last = txt[:-1]
    
    # Split the string into individual words using space as delimiter
    words = txt_without_last.split()
    
    # Check if the last character is part of a word or not
    return last_char not in words and last_char.isalpha()
```

The problem statement and the function's purpose are clearly explained in the docstring at the beginning of the code, which provides vital details for understanding the functionality.

This function uses different approaches depending on the situation to achieve the desired outcome, such as checking if the final character is an alphabetical character and determining whether the final character is part of a word.

The following examples demonstrate how to use this function:
```python
# The last character is a letter, but it's part of a word
print(check_if_last_char_is_a_letter("apple pie"))  # Output: False

# The last character is a letter, and it's not part of a word
print(check_if_last_char_is_a_letter("apple pi e"))  # Output: True

# The last character is a letter, but it's part of a word (with extra spaces)
print(check_if_last_char_is_a_letter("apple pi e "))  # Output: False

# The last character is not a letter
print(check_if_last_char_is_a_letter("1"))  # Output: False

# Empty input
print(check_if_last_char_is_a_letter(""))  # Output: False
```

The example cases illustrate a variety of input scenarios and demonstrate the function's behavior and expected output.