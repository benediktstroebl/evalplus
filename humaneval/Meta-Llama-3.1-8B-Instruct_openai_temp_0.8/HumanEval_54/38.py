### Same Characters Checker

Here's a Python script that checks if two words have the same characters.

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


if __name__ == "__main__":
    test_cases = [
        ("eabcdzzzz", "dddzzzzzzzddeddabc"),
        ("abcd", "dddddddabc"),
        ("dddddddabc", "abcd"),
        ("eabcd", "dddddddabc"),
        ("abcd", "dddddddabce"),
        ("eabcdzzzz", "dddzzzzzzzddddabc"),
    ]

    for s0, s1 in test_cases:
        print(f"same_chars('{s0}', '{s1}') -> {same_chars(s0, s1)}")
```

This script defines the `same_chars` function, which sorts the characters in each word and checks if the sorted lists are equal. The `if __name__ == "__main__":` block includes a set of test cases to verify the correctness of the function.