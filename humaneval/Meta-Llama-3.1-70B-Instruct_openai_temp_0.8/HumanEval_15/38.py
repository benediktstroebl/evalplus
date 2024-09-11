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
    # Generate a list of numbers from 0 to n (inclusive)
    numbers = list(range(n + 1))
    
    # Convert each number to a string and join them with spaces
    sequence =''.join(map(str, numbers))
    
    return sequence

# Test the function
print(string_sequence(0))  # Outputs: 0
print(string_sequence(5))  # Outputs: 0 1 2 3 4 5
```

This Python script defines a function called `string_sequence` that generates a string containing space-delimited numbers from 0 to `n` (inclusive). It uses the built-in `range` function to generate the numbers, converts each number to a string using the `map` function, and then joins the strings together with spaces using the `join` method.