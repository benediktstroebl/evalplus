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
    # Create dictionaries to store character counts for each string
    char_count_s0 = {}
    char_count_s1 = {}

    # Populate the dictionaries
    for char in s0:
        char_count_s0[char] = char_count_s0.get(char, 0) + 1
    for char in s1:
        char_count_s1[char] = char_count_s1.get(char, 0) + 1

    # Compare the dictionaries
    return char_count_s0 == char_count_s1

# Test cases
if same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'):
    print("Test passed!")
if same_chars('abcd', 'dddddddabc'):
    print("Test passed!")
if same_chars('dddddddabc', 'abcd'):
    print("Test passed!")
if not same_chars('eabcd', 'dddddddabc'):
    print("Test passed!")
if not same_chars('abcd', 'dddddddabce'):
    print("Test passed!")
if not same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'):
    print("Test passed!")
```

This script defines a function `same_chars` that takes two strings as input and returns `True` if they have the same characters, and `False` otherwise. The function works by counting the occurrences of each character in each string using dictionaries, and then comparing the two dictionaries for equality. If the dictionaries are equal, it means that the strings have the same characters, regardless of their order.