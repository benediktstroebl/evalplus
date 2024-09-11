```python
def below_threshold(l: list, t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(i <= t for i in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers `l` and a threshold value `t` as arguments. It returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the `all` function in combination with a generator expression to check each number in the list. If any number is not less than or equal to the threshold, the `all` function returns `False`.