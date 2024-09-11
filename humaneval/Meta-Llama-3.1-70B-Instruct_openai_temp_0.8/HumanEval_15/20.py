```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers in the sequence.
    """
    # Use a list comprehension to generate the sequence of numbers
    sequence = [str(i) for i in range(n + 1)]
    
    # Join the sequence into a string with spaces in between
    result =''.join(sequence)
    
    return result

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

Alternatively, you can also use the `map` function in conjunction with `join` to achieve the same result in one line:

```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers in the sequence.
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```