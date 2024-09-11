```python
def below_threshold(lst: list, threshold: int):
    """Return True if all numbers in the list lst are below threshold.
        False otherwise.

    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold to compare numbers with.

    Returns:
        bool: Whether all numbers in the list are below the threshold.
    """
    return all(num < threshold for num in lst)


# Test cases
if below_threshold([1, 2, 4, 10], 100):
    print("Test case 1 passed")
if not below_threshold([1, 20, 4, 10], 5):
    print("Test case 2 passed")
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold, and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The `all` function with a generator expression is used to check this condition. The test cases at the end check that the function behaves as expected.