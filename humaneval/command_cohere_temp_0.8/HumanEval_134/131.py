```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to analyze.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string to words and letters
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    words = txt.split()
    if len(words) == 0:
        # If the string contains only spaces
        return False
    elif len(words) == 1:  # Only 1 word
        return words[-1][-1] in letters
    else:
        # More than 1 word
        for i in range(len(words) - 1, -1, -1):
            if words[i][-1] in letters:
                return True
            elif words[i][-1] in ' ':
                continue
            else:
                return False

# Test cases
print(check_if_last_char_is_a_letter("apple pie"))  # Expected: False
print(check_if_last_char_is_a_letter("apple pi e"))  # Expected: True
print(check_if_last_char_is_a_letter("apple pi e "))  # Expected: False
print(check_if_last_char_is_a_letter(""))  # Expected: False
```

The function `check_if_last_char_is_a_letter` serves the purpose of checking whether the final character of a given string is an alphabetical character and is not a part of a word, including situations where the string ends with more than one word.

This is accomplished by splitting the input string into individual words and then examining the last character of each word until a word is found where the last character is an alphabetical character and is not preceded by a space. 

The test cases provided demonstrate the function's behavior on various input scenarios, including edge cases. The expected output for each case is specified within corresponding `print` statements.