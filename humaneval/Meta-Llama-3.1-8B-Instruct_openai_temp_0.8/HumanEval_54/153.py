```markdown
# Same Characters in Two Strings
=============================

This script checks if two words have the same characters.

### Function

```python
from collections import Counter

def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    Args:
        s0 (str): The first string.
        s1 (str): The second string.

    Returns:
        bool: True if the strings have the same characters, False otherwise.

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
    return Counter(s0) == Counter(s1)
```

### Example Usage

```python
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script uses the `Counter` class from the `collections` module to count the frequency of each character in both strings. If the two counters are equal, then the strings have the same characters. This approach has a time complexity of O(n), where n is the length of the strings.