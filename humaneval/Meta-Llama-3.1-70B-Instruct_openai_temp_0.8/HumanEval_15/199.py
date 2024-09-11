```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing the sequence of numbers.
    """
    # Generate a list of numbers from 0 to n (inclusive) and convert them to strings
    numbers = [str(i) for i in range(n + 1)]
    
    # Join the list of strings into a single string with spaces in between
    sequence =''.join(numbers)
    
    return sequence

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```