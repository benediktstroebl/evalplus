```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.
    
    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that generates a string sequence from 0 to `n` (inclusive) and returns it. The `join` method is used to concatenate the numbers in the sequence with spaces in between. The `map` function is used to convert each number in the sequence to a string, and the `range` function is used to generate the sequence. The test cases are included to verify the correctness of the function.