```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string of space-delimited numbers from 0 to n.

    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))


if __name__ == "__main__":
    # Test the function
    print(string_sequence(0))  # Output: 0
    print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

In this script, we define the `string_sequence` function that uses list comprehension and the `join` method to generate the string of space-delimited numbers. The `if __name__ == "__main__":` block is used to test the function with example inputs.