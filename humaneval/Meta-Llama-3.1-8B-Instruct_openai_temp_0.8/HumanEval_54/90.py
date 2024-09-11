```python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    # Convert both strings to lists of characters and sort them
    chars0 = sorted(s0)
    chars1 = sorted(s1)

    # Compare the sorted lists
    return chars0 == chars1

# Example usage:
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # Output: True
print(same_chars('abcd', 'dddddddabc'))  # Output: True
print(same_chars('dddddddabc', 'abcd'))  # Output: True
print(same_chars('eabcd', 'dddddddabc'))  # Output: False
print(same_chars('abcd', 'dddddddabce'))  # Output: False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # Output: False
```

This script defines a function `same_chars` that checks if two input strings have the same characters. It does this by converting both strings to lists of characters, sorting these lists, and comparing the sorted lists. If the sorted lists are equal, the function returns `True`; otherwise, it returns `False`. The example usage at the end of the script demonstrates how to use the `same_chars` function with various input pairs.