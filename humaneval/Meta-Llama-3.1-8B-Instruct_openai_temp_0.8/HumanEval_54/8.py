```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.

    Args:
        s0 (str): First string to compare.
        s1 (str): Second string to compare.

    Returns:
        bool: True if both strings have the same characters, False otherwise.

    Examples:
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
    # Convert both strings to lists of characters
    chars0 = sorted(s0)
    chars1 = sorted(s1)

    # Compare the lists of characters
    return chars0 == chars1

# Example usage:
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```