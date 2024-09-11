```markdown
## Same Characters Checker

### Problem Description

Check if two words have the same characters, disregarding their order.

### Code

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

### Explanation

This script defines a function `same_chars` that checks if two input strings have the same characters. It uses the `sorted` function to sort the characters in each string and compare the results. If the sorted strings are equal, it returns `True`, indicating that the original strings have the same characters. Otherwise, it returns `False`.

The test cases at the end of the script verify the function's correctness by checking the expected output for different input combinations.