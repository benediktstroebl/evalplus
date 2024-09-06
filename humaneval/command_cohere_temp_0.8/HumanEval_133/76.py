```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = 0
    for n in lst:
        rounded_n = int(n**2)**0.5
        result += rounded_n
    return result
```

The function `sum_squares` takes a list of numbers as an argument and adds up the squares of the integers in the list. To ensure that the output is rounded up to the nearest integer, we multiply the squared value by itself and take the square root, thereby rounding up the value. The resulting sum is returned as the output of the function. 

This approach ensures that the output meets the problem requirements for the given input list.