```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        lst (list): A list of elements.
    
    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

# Example use cases:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

In this script, the `monotonic` function checks if all elements in the list are either monotonically increasing (each element is less than or equal to the next) or monotonically decreasing (each element is greater than or equal to the next). It uses the `all` function in combination with a generator expression to check these conditions. If either condition is met, the function returns `True`; otherwise, it returns `False`.