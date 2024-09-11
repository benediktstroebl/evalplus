```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Example usage:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks whether the elements of a list are monotonically increasing or decreasing. It uses the `all` function with a generator expression to check if each element is either less than or equal to the next one (for increasing order), or greater than or equal to the next one (for decreasing order). If any pair of adjacent elements is out of order, the `all` function will return `False`. If all pairs of adjacent elements are in order, the `all` function will return `True`.