```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The end of the sequence.

    Returns:
        str: A string containing the sequence of numbers.
    """
    # Use a list comprehension to generate the sequence of numbers
    sequence = [str(i) for i in range(n + 1)]
    
    # Join the sequence into a string with spaces in between
    sequence_str =''.join(sequence)
    
    return sequence_str

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```