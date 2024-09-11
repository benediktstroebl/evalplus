```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(i < threshold for i in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
print(below_threshold([1, 2, 3, 4], 5))     # True
print(below_threshold([10, 20, 30], 5))     # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input and returns True if all numbers in the list are below the threshold, and False otherwise. The `all` function is used with a generator expression to check this condition. The `all` function returns True if all elements of the iterable (in this case, the generator expression) are True.