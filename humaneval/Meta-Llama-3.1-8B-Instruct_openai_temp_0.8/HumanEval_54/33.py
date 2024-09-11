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
    # Remove duplicate characters and convert to sets for comparison
    return sorted(set(s0)) == sorted(set(s1))


# Test cases
if __name__ == "__main__":
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    assert same_chars('abcd', 'dddddddabc')
    assert same_chars('dddddddabc', 'abcd')
    assert not same_chars('eabcd', 'dddddddabc')
    assert not same_chars('abcd', 'dddddddabce')
    assert not same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    print("All test cases pass")
```

This script defines a function `same_chars` that checks if two words have the same characters. It uses a trick where it removes duplicates and converts the strings to sets, which are unordered collections of unique elements. The function then compares these sets using the equality operator. If they are equal, it means the original strings have the same characters, regardless of their order and count. The script also includes test cases to verify the correctness of the function.