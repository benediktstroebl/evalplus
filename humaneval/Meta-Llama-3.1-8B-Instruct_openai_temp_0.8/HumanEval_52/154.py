```python
def below_threshold(l: list, t: int):
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of integers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list l are below threshold t, False otherwise.
    """
    # Use a generator expression within the all() function to check if all numbers in the list are below the threshold
    return all(num < t for num in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold()` that checks if all numbers in a given list `l` are below a specified threshold value `t`. It uses a generator expression within the `all()` function to efficiently check all numbers in the list. The `all()` function returns `True` if all elements in the iterable are true, and `False` if at least one element is false.