```markdown
# Same Characters Function

## Problem Description
This Python script provides a function `same_chars` that checks if two input strings have the same characters, regardless of order.

## Code
```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.

    Args:
        s0 (str): The first input string.
        s1 (str): The second input string.

    Returns:
        bool: True if the strings have the same characters, False otherwise.
    """
    # Remove spaces and convert to lowercase for case-insensitivity
    s0 = s0.replace(' ', '').lower()
    s1 = s1.replace(' ', '').lower()

    # Compare the sorted character sets of the two strings
    return sorted(set(s0)) == sorted(set(s1))

# Example use cases
if __name__ == "__main__":
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # Expected: True
    print(same_chars('abcd', 'dddddddabc'))  # Expected: True
    print(same_chars('dddddddabc', 'abcd'))  # Expected: True
    print(same_chars('eabcd', 'dddddddabc'))  # Expected: False
    print(same_chars('abcd', 'dddddddabce'))  # Expected: False
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # Expected: False
```

## Explanation

This function works by first removing any spaces from the input strings and converting them to lowercase for case-insensitivity. It then converts each string into a set of unique characters, sorts the sets, and compares them. If the sorted sets are equal, the function returns `True`, indicating that the input strings have the same characters. Otherwise, it returns `False`.
```