```python
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    
    Args:
    l (list): A list of numbers.
    t (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    # Use built-in all() function and a generator expression to check if all numbers in the list are below the threshold
    return all(num < t for num in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, the `below_threshold` function uses the `all()` function in combination with a generator expression to check if all numbers in the list `l` are below the threshold `t`. The `all()` function returns `True` if all elements of the iterable are true, and `False` otherwise. In this case, the iterable is a generator expression that yields `True` for each number in the list that is below the threshold. If any number in the list is not below the threshold, `all()` will return `False`, which is the desired result.