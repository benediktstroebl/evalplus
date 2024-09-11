```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of numbers
        threshold (int): The threshold value
    
    Returns:
        bool: True if all numbers in lst are below threshold, False otherwise
    """
    return all(num < threshold for num in lst)

# Example use cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

In this script, we use the built-in `all()` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements of the iterable are true. If at least one element is false, it returns `False`.