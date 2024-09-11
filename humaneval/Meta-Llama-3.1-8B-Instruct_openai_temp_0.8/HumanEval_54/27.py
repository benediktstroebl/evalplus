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
    return sorted(s0) == sorted(s1)


# Test cases
if same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') and same_chars('abcd', 'dddddddabc') and same_chars('dddddddabc', 'abcd'):
    print("Test case 1: Success")
else:
    print("Test case 1: Failure")

if not same_chars('eabcd', 'dddddddabc') and not same_chars('abcd', 'dddddddabce'):
    print("Test case 2: Success")
else:
    print("Test case 2: Failure")

if not same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'):
    print("Test case 3: Success")
else:
    print("Test case 3: Failure")
```

This script defines the `same_chars` function, which takes two strings `s0` and `s1` as input and returns `True` if they have the same characters, regardless of their order, and `False` otherwise. It uses the `sorted` function to sort the characters in each string and then compares the sorted lists.

The test cases at the end of the script check the function's correctness based on the provided docstring.