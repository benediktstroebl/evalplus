```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers.
    """
    # Use a list comprehension to generate a list of numbers from 0 to n
    numbers = [str(i) for i in range(n + 1)]
    
    # Join the list of numbers into a string with spaces in between
    sequence =''.join(numbers)
    
    return sequence

# Test the function
print(string_sequence(0))  # Should print: 0
print(string_sequence(5))  # Should print: 0 1 2 3 4 5
```

Alternatively, you can use a more concise version:

```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Should print: 0
print(string_sequence(5))  # Should print: 0 1 2 3 4 5
```