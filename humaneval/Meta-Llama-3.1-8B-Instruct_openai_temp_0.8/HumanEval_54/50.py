```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    
    Args:
        s0 (str): The first word.
        s1 (str): The second word.
        
    Returns:
        bool: True if the words have the same characters, False otherwise.
    """
    # Remove duplicate characters from both words by converting them to sets
    set0 = set(s0)
    set1 = set(s1)
    
    # Check if the sets are equal
    return set0 == set1


# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script defines a function `same_chars` that checks if two input strings have the same characters. It does this by converting the strings to sets, which automatically removes duplicate characters, and then checks if the two sets are equal. The `same_chars` function is then tested with the provided test cases.