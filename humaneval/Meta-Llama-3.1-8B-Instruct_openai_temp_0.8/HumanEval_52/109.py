```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(i < threshold for i in lst)


# Test cases
if below_threshold([1, 2, 4, 10], 100):
    print("Test case 1 passed")
if not below_threshold([1, 20, 4, 10], 5):
    print("Test case 2 passed")
```

This script defines a function `below_threshold` that checks if all numbers in the given list are below the specified threshold. The function uses the built-in Python `all` function with a generator expression to achieve this. The `all` function returns `True` if all elements in the iterable (in this case, the generator expression) are `True`, otherwise it returns `False`. If any element in the generator expression is not less than the threshold, the `all` function will return `False`.

The script also includes two test cases to verify the function's correctness.