### Solution: below_threshold Function
```python
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    
    Args:
    l (list): A list of numbers.
    t (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list l are below threshold t.
    
    Example:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(i < t for i in l)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```
This script defines a function `below_threshold` that checks if all numbers in a given list are below a certain threshold. The function uses the built-in `all` function in combination with a generator expression to check each number in the list. If a number is not less than the threshold, the `all` function will return `False`. If all numbers in the list are below the threshold, the `all` function will return `True`.