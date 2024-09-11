```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: Whether all numbers in the list are below the threshold.
    """
    return all(num < threshold for num in lst)

# Testing the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks whether all numbers in a list are below a specified threshold. It uses Python's built-in `all` function in combination with a generator expression to achieve this. The `all` function returns `True` if all elements in the iterable (in this case, the generator expression) are true. If at least one element is false, it returns `False`. 

In the generator expression `num < threshold for num in lst`, `num` represents each number in the list, and the expression `num < threshold` checks whether each number is below the threshold. 

Finally, the script includes two test cases to demonstrate the function's usage.