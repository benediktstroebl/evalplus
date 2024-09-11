```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.

    Args:
        s0 (str): First word.
        s1 (str): Second word.

    Returns:
        bool: True if the words have the same characters, False otherwise.
    """
    # Remove any whitespace from the input strings
    s0 = s0.replace(" ", "")
    s1 = s1.replace(" ", "")

    # Create a sorted list of characters for each string
    sorted_s0 = sorted(s0)
    sorted_s1 = sorted(s1)

    # Compare the sorted lists
    return sorted_s0 == sorted_s1


# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script uses the sorted() function in Python to sort the characters in each string and then compares the sorted lists. If the lists are equal, the function returns True; otherwise, it returns False.