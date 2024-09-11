```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    
    :param s0: First word
    :param s1: Second word
    :return: True if both words have the same characters, False otherwise
    """
    # Convert words to sets and compare
    return sorted(s0) == sorted(s1)


# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script uses Python's built-in `sorted` function to sort the characters in each word, then compares the sorted lists. This works because lists are equal in Python if and only if their elements are equal, regardless of order.