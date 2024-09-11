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
    # Remove duplicate characters from each word and compare the results
    return set(s0.lower()) == set(s1.lower())

# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # Expected: True
print(same_chars('abcd', 'dddddddabc'))  # Expected: True
print(same_chars('dddddddabc', 'abcd'))  # Expected: True
print(same_chars('eabcd', 'dddddddabc'))  # Expected: False
print(same_chars('abcd', 'dddddddabce'))  # Expected: False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # Expected: False
```

This script defines a function `same_chars` that takes two strings as input and returns `True` if they have the same characters (ignoring case and order), and `False` otherwise. The function uses a `set` to remove duplicate characters from each word, and then compares the resulting sets for equality. The test cases at the end demonstrate the function's behavior with various inputs.