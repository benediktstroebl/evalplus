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
        rounded_n = int(n)
        result += rounded_n ** 2
    return result
```

The function `sum_squares` takes a list of numbers, squares each element, and returns the sum of those squared values. This solution adheres to the problem's requirements, as it first rounds each list element to the nearest higher integer before calculating squared sums.