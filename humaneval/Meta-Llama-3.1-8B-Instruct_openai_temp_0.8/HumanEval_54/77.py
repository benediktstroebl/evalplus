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
    # Create a sorted list of characters from both words and compare them
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

This script defines a function `same_chars` that checks if two strings have the same characters. It uses the `sorted` function to create a sorted list of characters from both strings and compares these lists. The function returns `True` if the lists are equal and `False` otherwise.

The test cases at the end of the script verify that the `same_chars` function works correctly.