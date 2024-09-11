```python
def below_threshold(l: list, t: int):
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
    l (list): A list of integers.
    t (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.

    Examples:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(x < t for x in l)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines the `below_threshold` function, which takes a list of integers and a threshold value as input and returns a boolean indicating whether all numbers in the list are below the threshold. The `all` function is used with a generator expression to check if all elements in the list meet the condition. The script also includes example use cases to demonstrate the function's behavior.