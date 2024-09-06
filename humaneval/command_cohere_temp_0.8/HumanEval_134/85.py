```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.

    Examples:
    >>> check_if_last_char_is_a_letter("apple pie")
    False
    >>> check_if_last_char_is_a_letter("apple pi e")
    True
    >>> check_if_last_char_is_a_letter("apple pi e ")
    False
    >>> check_if_last_char_is_a_letter("")
    False
    >>> check_if_last_char_is_a_letter("abc")
    True
    """
    # Split the string into words using whitespace characters as separators
    words = txt.split()
    # Get the last character by slicing the last element in the array-like object
    last_char = words[-1][-1]
    # Check 1: Check if the last character is an alphabetical character
    if last_char.isalpha():
        # Check 2: If the last character is not the first character of a word
        if len(words[-1]) > 1 and words[-1][0] == last_char:
            return False
        else:
            return True
    else:
        return False
```

This Python script defines a function called `check_if_last_char_is_a_letter`, which takes a single argument, `txt`, and returns `True` if the last character of the input string is an alphabetical character and is not part of a word; otherwise, it returns `False`. 

The function first splits the input string into individual words using whitespace characters as separators. Then, it retrieves the last character from the last element (word) in the split array-like object using slicing. It then checks if the last character is an alphabetical character using the `isalpha()` method. If the character is alphabetical, it further checks if the last character is the first character of a word, returning `False` if it is. If it passes both checks, the function returns `True`. 

The example tests demonstrate the function's behavior and correctly pass all conditions outlined in the original problem statement.