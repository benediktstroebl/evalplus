```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Ensure the input string is not empty
    if not txt:
        return False

    # Split the string into individual words
    words = txt.split()
    # If the last character is a word character but not the first character of the last word, it is ok.
    # If it is the first character of the last word, it is not ok.
    return (words[-1][-1].isalpha() and words[-1][-1] != words[-1][0]) or (len(words) == 0)
``` 

The test cases are provided below:
```python
# Test Case 1
print(check_if_last_char_is_a_letter("apple pie"))  # Expected output: False

# Test Case 2
print(check_if_last_char_is_a_letter("apple pi e"))  # Expected output: True

# Test Case 3
print(check_if_last_char_is_a_letter("apple pi e "))  # Expected output: False

# Test Case 4
print(check_if_last_char_is_a_letter(""))  # Expected output: False
```

To test the function, simply call it with the input text specified in the prompt, and the function should return the expected boolean values.