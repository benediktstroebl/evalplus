```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The upper limit of the sequence.
    
    Returns:
    str: A string containing space-delimited numbers from 0 to n.
    """
    
    # Use a list comprehension to generate a list of numbers from 0 to n
    sequence = [str(i) for i in range(n + 1)]
    
    # Join the list of numbers into a single string with spaces in between
    sequence_str =''.join(sequence)
    
    return sequence_str


# Test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```