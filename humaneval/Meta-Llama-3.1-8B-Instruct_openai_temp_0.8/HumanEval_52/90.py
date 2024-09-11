```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < threshold for num in lst)


# Example usage
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))  # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value, and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the built-in `all` function in combination with a generator expression to check this condition. The `all` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. The generator expression `num < threshold for num in lst` yields `True` for each number in the list that is below the threshold, and `False` otherwise. If all numbers in the list are below the threshold, `all` will return `True`; otherwise, it will return `False`.

The example usage at the bottom of the script demonstrates how to use the `below_threshold` function with different inputs.