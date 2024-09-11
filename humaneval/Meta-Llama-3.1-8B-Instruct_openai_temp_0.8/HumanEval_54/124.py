```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.

    Args:
        s0 (str): The first word.
        s1 (str): The second word.

    Returns:
        bool: True if both words have the same characters, False otherwise.
    """
    return sorted(s0) == sorted(s1)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ('eabcdzzzz', 'dddzzzzzzzddeddabc'),
        ('abcd', 'dddddddabc'),
        ('dddddddabc', 'abcd'),
        ('eabcd', 'dddddddabc'),
        ('abcd', 'dddddddabce'),
        ('eabcdzzzz', 'dddzzzzzzzddddabc')
    ]

    for test_case in test_cases:
        result = same_chars(*test_case)
        print(f"Test case: {test_case[0]} and {test_case[1]}. Result: {result}")
```

This script defines a function `same_chars` that takes two strings as input and returns `True` if they have the same characters, regardless of the order, and `False` otherwise. The function uses the `sorted` function to sort the characters in each string and compares the resulting lists. If the lists are equal, the original strings have the same characters.

The script also includes a test suite to verify the correctness of the `same_chars` function. The test suite uses the same test cases as the original problem statement and prints the result of each test case.

Note: This script uses the `*` operator to unpack the test case tuple into two separate arguments for the `same_chars` function. This is a common Python idiom for passing multiple arguments to a function.