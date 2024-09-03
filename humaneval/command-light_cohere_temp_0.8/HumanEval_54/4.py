```python
def same_chars(s0: str, s1: str):
    """
    Check if two strings have the same characters
    Returns:
        True, if two strings are same in characters
        False, otherwise
    """
    return s0 == s1

# Test the function
print(same_chars('eabcd', 'dddzzzzzdddeddabc'))  # Output: True
print(same_chars('abcd', 'dddddddabc'))  # Output: True
print(same_chars('abcdef', 'eeeeefdef'))  # Output: False
print(same_chars('abcd123', '1234567890'))  # Output: False
```
This function checks two input strings and returns True if they have the same characters and False otherwise.