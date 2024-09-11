```python
from collections import Counter

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    
    Args:
        s0 (str): The first word.
        s1 (str): The second word.
    
    Returns:
        bool: True if the words have the same characters, False otherwise.
    """
    # Remove duplicate characters and convert to lowercase
    s0_count = Counter(s0.lower())
    s1_count = Counter(s1.lower())
    
    # Check if the two word's characters counters are equal
    return s0_count == s1_count

# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script defines a function `same_chars` that checks if two input strings have the same characters. It uses the `Counter` class from the `collections` module to count the occurrences of each character in each string, then compares these two character counts. If they are equal, the strings have the same characters; otherwise, they do not. The test cases at the end demonstrate the function's behavior.