```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))  # include n in the sequence


# Test the function
if __name__ == "__main__":
    print(string_sequence(0))  # Output: '0'
    print(string_sequence(5))  # Output: '0 1 2 3 4 5'
    print(string_sequence(10))  # Output: '0 1 2 3 4 5 6 7 8 9 10'
```

This script defines the `string_sequence` function as per the provided specification. It uses the `join` method to concatenate the numbers in the range from 0 to `n` (inclusive) into a string, with spaces between each number. The `map` function is used to convert each number in the range to a string, so they can be joined together. 

The script also includes a test section at the end to demonstrate the function's behavior with different inputs.