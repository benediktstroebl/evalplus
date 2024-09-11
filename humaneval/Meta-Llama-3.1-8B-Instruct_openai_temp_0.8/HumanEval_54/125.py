```python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    Args:
    s0 (str): The first word.
    s1 (str): The second word.

    Returns:
    bool: True if two words have the same characters, False otherwise.
    """
    # Remove duplicate characters from the first string
    set0 = set(s0)
    # Remove duplicate characters from the second string
    set1 = set(s1)
    # Compare the two sets. If they are equal, the strings have the same characters.
    return set0 == set1


# Test cases
if same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'):
    print("Test 1 passed")
if same_chars('abcd', 'dddddddabc'):
    print("Test 2 passed")
if same_chars('dddddddabc', 'abcd'):
    print("Test 3 passed")
if not same_chars('eabcd', 'dddddddabc'):
    print("Test 4 passed")
if not same_chars('abcd', 'dddddddabce'):
    print("Test 5 passed")
if not same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'):
    print("Test 6 passed")
```

This script defines a function `same_chars` that takes two strings and returns True if they have the same characters, and False otherwise. The function works by converting the input strings into sets, which automatically removes any duplicate characters. It then compares the two sets to determine if they are equal. If they are equal, the function returns True, indicating that the strings have the same characters. If they are not equal, the function returns False. 

The test cases at the end of the script verify that the `same_chars` function behaves as expected.