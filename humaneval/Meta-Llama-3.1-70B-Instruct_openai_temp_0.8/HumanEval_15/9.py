```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))


# Example usage:
if __name__ == "__main__":
    print(string_sequence(0))  # Output: 0
    print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

In this script, we define the `string_sequence` function which uses a generator expression to create a sequence of numbers from 0 to `n` (inclusive), converts each number to a string, and joins them together with spaces in between. 

The `if __name__ == "__main__":` block is used to provide example usage of the function when the script is run directly.