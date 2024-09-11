```markdown
## Same Characters Checker

This script checks if two input strings have the same characters, regardless of order.

```python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    Args:
        s0 (str): First input string.
        s1 (str): Second input string.

    Returns:
        bool: True if the strings have the same characters, False otherwise.

    Example:
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
    # Convert both strings to sets to remove duplicate characters and ignore order
    set0 = set(s0)
    set1 = set(s1)
    
    # Compare the two sets
    return set0 == set1

# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script defines a function `same_chars` that takes two input strings `s0` and `s1`. It converts both strings to sets, which automatically removes duplicate characters and ignores order. It then compares the two sets and returns `True` if they are equal, and `False` otherwise. The script includes example test cases to demonstrate the function's behavior.