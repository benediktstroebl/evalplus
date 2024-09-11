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
    
    # Join the numbers into a string with space delimiter
    return''.join(numbers)


# Test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines the `string_sequence` function that takes an integer `n` and returns a string of space-delimited numbers from 0 to `n`. It uses list comprehension to generate the list of numbers, converts them to strings, and then joins them into a single string with space delimiter. The test cases at the end verify the function's correctness.