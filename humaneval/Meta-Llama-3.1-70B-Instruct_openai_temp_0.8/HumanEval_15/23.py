```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    # Generate a list of numbers from 0 to n using list comprehension
    numbers = [str(i) for i in range(n + 1)]
    
    # Join the numbers in the list into a string with spaces in between
    result =''.join(numbers)
    
    return result

# Test cases
print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The function uses list comprehension to generate the list of numbers and then joins them into a string with spaces in between. The test cases are included to demonstrate the function's behavior.