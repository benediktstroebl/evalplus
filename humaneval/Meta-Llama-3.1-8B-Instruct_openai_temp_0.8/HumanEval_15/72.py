```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The number up to which the sequence is generated.

    Returns:
        str: A string containing space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))


# Test the function
if __name__ == "__main__":
    print(string_sequence(0))
    print(string_sequence(5))
```

This script defines a function `string_sequence(n)` that generates a string containing space-delimited numbers from 0 to `n` inclusive. The `join()` method is used to concatenate the numbers into a single string. The example use cases are demonstrated in the docstring and also printed out when the script is run.