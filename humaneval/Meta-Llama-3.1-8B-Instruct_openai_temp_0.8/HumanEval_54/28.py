```python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    
    Args:
    s0 (str): The first word.
    s1 (str): The second word.
    
    Returns:
    bool: True if the two words have the same characters, False otherwise.
    """
    # Remove spaces and sort characters in both strings
    s0 = ''.join(sorted(set(s0.replace(' ', ''))))
    s1 = ''.join(sorted(set(s1.replace(' ', ''))))
    
    # Compare the sorted strings
    return s0 == s1

# Test cases
assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
assert same_chars('abcd', 'dddddddabc')
assert same_chars('dddddddabc', 'abcd')
assert not same_chars('eabcd', 'dddddddabc')
assert not same_chars('abcd', 'dddddddabce')
assert not same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
```

This script defines a function `same_chars` that takes two strings `s0` and `s1` as input, removes any spaces from the strings, sorts the characters in each string, and then compares the sorted strings. If the sorted strings are equal, the function returns `True`, indicating that the original strings have the same characters. Otherwise, it returns `False`. The script includes the provided test cases to demonstrate the function's correctness.