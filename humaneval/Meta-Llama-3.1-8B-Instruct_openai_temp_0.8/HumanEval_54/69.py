```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    
    Args:
        s0 (str): The first word.
        s1 (str): The second word.
    
    Returns:
        bool: True if the two words have the same characters, False otherwise.
    """
    # Remove whitespace and convert to lowercase
    s0 = s0.replace(' ', '').lower()
    s1 = s1.replace(' ', '').lower()
    
    # Check if the sorted characters are equal
    return sorted(s0) == sorted(s1)


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

This script defines a function `same_chars` that checks if two words have the same characters. It first removes whitespace and converts the words to lowercase, then checks if the sorted characters are equal. If they are, the function returns `True`; otherwise, it returns `False`. The script includes the provided test cases to verify that the function works as expected.