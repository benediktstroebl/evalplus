```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers.
    """
    # Generate a list of numbers from 0 to n using list comprehension
    numbers = [str(i) for i in range(n + 1)]
    
    # Join the numbers in the list into a string separated by spaces
    result =''.join(numbers)
    
    return result

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```