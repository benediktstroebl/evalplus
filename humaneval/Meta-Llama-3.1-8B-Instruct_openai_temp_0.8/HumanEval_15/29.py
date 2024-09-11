Here is the self-contained Python script that solves the problem:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the number sequence.
    
    Returns:
        str: A string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```
This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 to `n` inclusive. The function uses the `join` method and `map` function to convert the numbers to strings and then join them with spaces. The script also includes example usage and test cases to demonstrate the function's behavior.