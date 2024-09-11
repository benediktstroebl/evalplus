```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))


# Example usage:
if __name__ == "__main__":
    print(string_sequence(0))  # Output: 0
    print(string_sequence(5))  # Output: 0 1 2 3 4 5
    print(string_sequence(10))  # Output: 0 1 2 3 4 5 6 7 8 9 10
```

In this script, the `string_sequence` function uses the `join` method and `map` function to generate a string containing the numbers from 0 to `n` (inclusive), separated by spaces. The `range(n + 1)` function generates a sequence of numbers from 0 to `n`, and `map(str,...)` converts these numbers to strings, which can then be joined together with spaces using `' '.join(...)`. 

The script also includes example usage in the `if __name__ == "__main__":` block, which shows how to use the `string_sequence` function to generate sequences of different lengths.