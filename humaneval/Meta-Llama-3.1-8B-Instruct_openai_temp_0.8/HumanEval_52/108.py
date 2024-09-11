```python
def below_threshold(l: list, t: int):
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(i < t for i in l)


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines the `below_threshold` function, which takes a list `l` and an integer `t` as arguments. It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements in the iterable (in this case, the generator expression) are `True`, and `False` otherwise.

The script also includes test cases to verify that the function works as expected.