```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers starting from 0 upto n inclusive.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This Python script defines a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 up to `n` inclusive. The function uses a generator expression to generate the numbers and the `join()` method to concatenate them into a single string. The test cases at the end demonstrate the function's behavior.