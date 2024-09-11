```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n inclusive.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    # Use a list comprehension to generate a list of numbers from 0 to n
    numbers = [str(i) for i in range(n + 1)]
    
    # Join the numbers in the list with spaces to form the output string
    output =''.join(numbers)
    
    return output

# Test the function
print(string_sequence(0))
print(string_sequence(5))
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. It uses a list comprehension to generate the list of numbers, and the `join` method to concatenate the numbers with spaces. The script also includes example usage of the function.