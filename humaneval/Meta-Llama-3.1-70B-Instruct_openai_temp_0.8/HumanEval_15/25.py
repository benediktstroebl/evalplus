```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
if __name__ == "__main__":
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    print("All tests passed.")
```

In this script, we define the `string_sequence` function that takes an integer `n` and returns a string of space-delimited numbers from 0 to `n` inclusive. We use the `range` function to generate the sequence of numbers and `map` to convert each number to a string. The `join` method is then used to concatenate the strings with spaces in between.

The script also includes test cases to verify that the function works correctly. If all tests pass, it prints "All tests passed."