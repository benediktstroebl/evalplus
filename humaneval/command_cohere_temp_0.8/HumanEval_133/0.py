```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): List of numbers.
    
    Returns:
        int: Sum of squared integers.
    """
    result = 0
    for n in lst:
        if isinstance(n, int): 
            result += n ** 2
    return result
```

The function iterates over each list item, checks if it is an integer, and accumulates the sum of squares of these integers accordingly. 

To handle the ceiling rounding, you can modify the function to round each number before calculating its square:
```python
def sum_squares_rounded(lst):
    """
    Return the sum of squared integers in the list, rounding each number first.
    
    Args:
        lst (list): List of numbers.
    
    Returns:
        int: Sum of squared integers.
    """
    result = 0
    for n in lst:
        if isinstance(n, (int, float)):
            n = ceil(n)  # Round each number to the upper integer
            result += n ** 2  # Calculate the squared sum
    return result
``` 

This approach ensures that each number is rounded up to the nearest integer before calculating its square.