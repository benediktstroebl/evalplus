```python
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    
    Args:
        l (list): A list of integers to check.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(i < t for i in l)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of integers `l` and a threshold value `t` as arguments. It returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The `all` function in Python is used to check if all elements of a given iterable are true. The generator expression `(i < t for i in l)` generates a boolean value for each number in the list indicating whether it is below the threshold. The `all` function then returns `True` if all these boolean values are `True`.