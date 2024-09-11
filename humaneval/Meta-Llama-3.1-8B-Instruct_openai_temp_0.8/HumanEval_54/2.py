```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.

    Args:
        s0 (str): The first word.
        s1 (str): The second word.

    Returns:
        bool: True if the words have the same characters, False otherwise.

    Examples:
        >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
        True
        >>> same_chars('abcd', 'dddddddabc')
        True
        >>> same_chars('dddddddabc', 'abcd')
        True
        >>> same_chars('eabcd', 'dddddddabc')
        False
        >>> same_chars('abcd', 'dddddddabce')
        False
        >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
        False
    """
    # Create two dictionaries to count the occurrences of each character
    char_count_s0 = {}
    char_count_s1 = {}

    # Count the occurrences of each character in the first string
    for char in s0:
        if char in char_count_s0:
            char_count_s0[char] += 1
        else:
            char_count_s0[char] = 1

    # Count the occurrences of each character in the second string
    for char in s1:
        if char in char_count_s1:
            char_count_s1[char] += 1
        else:
            char_count_s1[char] = 1

    # The two strings have the same characters if and only if their character count dictionaries are equal
    return char_count_s0 == char_count_s1


# Test the function
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script defines a function `same_chars` that checks if two input strings have the same characters. It uses two dictionaries to count the occurrences of each character in both strings, and then compares these dictionaries to determine if the strings have the same characters. The script also includes example use cases to test the function.