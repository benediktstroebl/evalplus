```python
from collections import Counter

def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    Args:
    s0 (str): The first string.
    s1 (str): The second string.

    Returns:
    bool: True if the two strings have the same characters, False otherwise.
    """
    # Remove duplicates and count character frequency
    freq0 = Counter(s0)
    freq1 = Counter(s1)

    # Compare the frequency counts
    return freq0 == freq1


# Test cases
if same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'):
    print("Test case 1 passed")
if same_chars('abcd', 'dddddddabc'):
    print("Test case 2 passed")
if same_chars('dddddddabc', 'abcd'):
    print("Test case 3 passed")
if not same_chars('eabcd', 'dddddddabc'):
    print("Test case 4 passed")
if not same_chars('abcd', 'dddddddabce'):
    print("Test case 5 passed")
if not same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'):
    print("Test case 6 passed")
```

This script uses the `Counter` class from the `collections` module to count the frequency of each character in both strings. It then compares these frequency counts to determine if the two strings have the same characters.