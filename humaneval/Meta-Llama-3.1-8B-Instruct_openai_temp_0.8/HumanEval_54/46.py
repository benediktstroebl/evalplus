```python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    Args:
        s0 (str): The first word.
        s1 (str): The second word.

    Returns:
        bool: True if both words have the same characters, False otherwise.
    """
    # Remove spaces and convert both strings to lists of characters
    s0 = s0.replace(' ', '')
    s1 = s1.replace(' ', '')

    # Sort both lists and compare them
    return sorted(s0) == sorted(s1)


# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script defines a function `same_chars` that takes two strings `s0` and `s1` and returns `True` if they have the same characters, and `False` otherwise. The function first removes any spaces from the strings, then converts them to lists of characters. It sorts both lists and compares them for equality. If the sorted lists are equal, the function returns `True`; otherwise, it returns `False`. The script includes several test cases to demonstrate the function's behavior.