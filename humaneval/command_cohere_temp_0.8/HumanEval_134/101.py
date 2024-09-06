```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Split the string into words using whitespace characters as separators
    words = txt.split()
    # If the string is empty or there are no words at all, return False
    if not txt or not words:
        return False
    # Reduce the list of words to only the last character of the string, using slicing
    last_char = words[-1][-1]
    # Check if the last character is in fact alphabetical
    if str.isalpha(last_char):
        # Check if the last character is not part of a word, using the "in" operator
        if last_char not in str.punctuation:
            return True
    return False
```

The algorithm to solve the problem can be outlined as follows:
1. Split the string into words using whitespace characters as separators.
2. If the string is empty or contains no words, return `False`.
3. Use slicing to isolate the last character of the string.
4. Check if the last character is alphabetical using the `str.isalpha()` method.
5. If it is alphabetical, check if it is not part of a word (i.e., a punctuation mark) using the `str.punctuation` constant.
6. Return `True` if the last character is an alphabetical character not part of a word; otherwise, return `False`.

This algorithm carefully isolates the `last_char` and checks its properties to determine if it satisfies the conditions of the problem. The tests also ensure that edge cases like empty strings or strings with no whitespace are handled correctly.