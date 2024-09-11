Here's a Python function that uses a set to check if two words have the same characters:

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
    # Remove duplicate characters from each word
    s0_set = set(s0)
    s1_set = set(s1)
    
    # Check if the sets are equal (i.e., the words have the same characters)
    return s0_set == s1_set

# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This function works by creating sets of characters from each word, which automatically removes duplicate characters. It then checks if the two sets are equal. If they are, it means that the words have the same characters, so the function returns True. Otherwise, it returns False.