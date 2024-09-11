```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.

    Args:
        s0 (str): First word.
        s1 (str): Second word.

    Returns:
        bool: True if the two words have the same characters, False otherwise.

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
    # Remove spaces and sort characters in each word
    s0 = ''.join(sorted(set(s0.replace(' ', ''))))
    s1 = ''.join(sorted(set(s1.replace(' ', ''))))

    # Compare the two sets of characters
    return s0 == s1
```

This script works by first removing any spaces from the input strings, then sorting the characters in each string and removing any duplicates (since sets in Python are unordered collections of unique elements, they're perfect for this task). Finally, it compares the two sets of characters and returns True if they're equal, and False otherwise.