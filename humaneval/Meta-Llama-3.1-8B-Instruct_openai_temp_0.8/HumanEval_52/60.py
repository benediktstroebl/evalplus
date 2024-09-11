```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold threshold.
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in lst are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Test cases
if below_threshold([1, 2, 4, 10], 100):
    print("Test case 1 passed")
else:
    print("Test case 1 failed")

if not below_threshold([1, 20, 4, 10], 5):
    print("Test case 2 passed")
else:
    print("Test case 2 failed")
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as arguments. It uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements in the iterable are true, and `False` otherwise. If the function returns `True`, it means all numbers in the list are below the threshold.