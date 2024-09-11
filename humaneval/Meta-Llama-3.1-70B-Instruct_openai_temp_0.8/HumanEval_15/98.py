```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence (inclusive).
    
    Returns:
        str: A string containing space-delimited numbers starting from 0 upto n.
    """
    
    # Use a list comprehension to generate numbers from 0 to n
    numbers = [str(i) for i in range(n + 1)]
    
    # Join the numbers into a string with spaces in between
    sequence =''.join(numbers)
    
    return sequence

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```