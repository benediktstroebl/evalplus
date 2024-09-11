```python
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    
    Args:
    l (list): A list of numbers.
    t (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.

    Examples:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Use the built-in all() function in combination with a generator expression
    # to check if all numbers in the list are below the threshold
    return all(i < t for i in l)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function called `below_threshold` that takes a list of numbers (`l`) and a threshold value (`t`) as arguments. It returns `True` if all numbers in the list are below the threshold and `False` otherwise. The function uses the `all()` function in combination with a generator expression to check if all numbers in the list meet the condition. The script then tests the function with two examples.