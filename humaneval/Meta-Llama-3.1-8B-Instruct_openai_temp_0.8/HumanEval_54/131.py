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
    # Remove duplicates by converting to a set, and sort the characters
    # If the sorted sets are equal, then the words have the same characters
    return sorted(set(s0)) == sorted(set(s1))

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
This script defines a function `same_chars` that checks if two input strings have the same characters. It removes duplicates from the strings by converting them to sets, sorts the characters, and then compares the sorted sets. The test cases are included to verify that the function works correctly.