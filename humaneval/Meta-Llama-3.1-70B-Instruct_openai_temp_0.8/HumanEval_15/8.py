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
    return''.join(str(i) for i in range(n + 1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The function uses a generator expression to generate the numbers and the `join` method to concatenate them into a string.

The script also includes a docstring that provides documentation for the function, including its parameters, return value, and examples of usage.

The `if __name__ == "__main__":` block is used to run the `doctest` module, which tests the function using the examples provided in the docstring. If the function is working correctly, the script will run without any output. If the function is incorrect, the script will raise an exception.