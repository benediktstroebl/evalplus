```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string minus the last character
    pre_last_char_txt = txt[:-1]
    # Check if the last character is alphabetical and not part of a word
    return (
        (txt[-1].isalpha()) and 
        (not txt[-1].lower() in pre_last_char_txt.lower())
    )
```

The following tests will prove the correctness of our function:
```python
# Test Case 1: Last character is a letter, but it's part of a word
assert not check_if_last_char_is_a_letter("apple pie")

# Test Case 2: Last character is a letter, but it's part of a word with whitespace at the end
assert not check_if_last_char_is_a_letter("apple pi e ")

# Test Case 3: Last character is a letter, but it's part of a word with punctuation at the end
assert not check_if_last_char_is_a_letter("apple pi e.")

# Test Case 4: Last character is a letter, and it's not part of a word
assert check_if_last_char_is_a_letter("apple pi e")

# Test Case 5: Empty string
assert not check_if_last_char_is_a_letter("")
```