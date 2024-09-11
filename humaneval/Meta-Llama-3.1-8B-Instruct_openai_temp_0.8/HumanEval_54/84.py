```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    
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
    
    # Convert the strings to sets to remove duplicates and ignore order
    set0 = set(s0)
    set1 = set(s1)
    
    # Check if the two sets are equal
    return set0 == set1

# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # Expected output: True
print(same_chars('abcd', 'dddddddabc'))  # Expected output: True
print(same_chars('dddddddabc', 'abcd'))  # Expected output: True
print(same_chars('eabcd', 'dddddddabc'))  # Expected output: False
print(same_chars('abcd', 'dddddddabce'))  # Expected output: False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # Expected output: False
```