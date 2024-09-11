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
    # Remove duplicate characters in each word and convert to lowercase
    s0_chars = sorted(set(s0.lower()))
    s1_chars = sorted(set(s1.lower()))

    # Compare the two lists of unique characters
    return s0_chars == s1_chars


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

This script defines the `same_chars` function, which takes two strings as input and returns True if they have the same characters (ignoring order and case), and False otherwise. The test cases at the end verify the function's correctness.