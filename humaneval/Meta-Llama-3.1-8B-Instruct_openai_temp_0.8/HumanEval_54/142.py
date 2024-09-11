### Same Characters Checker
#### Script that checks if two words have the same characters

```python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    Args:
        s0 (str): The first word.
        s1 (str): The second word.

    Returns:
        bool: True if the words have the same characters, False otherwise.
    """
    # Convert each word into a set of characters, which automatically removes duplicates
    s0_chars = set(s0)
    s1_chars = set(s1)
    
    # Compare the two sets of characters
    return s0_chars == s1_chars


# Example usage:
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script uses the `set` data structure in Python, which is an unordered collection of unique elements. By converting each word into a set of characters, we can automatically remove any duplicate characters and then compare the two sets to determine if the words have the same characters. The `==` operator can be used to compare two sets, and it will return `True` if the sets are equal and `False` otherwise.