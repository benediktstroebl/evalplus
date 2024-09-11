Here's a Python script with the function `below_threshold` implemented:
```python
def below_threshold(lst: list, threshold: int):
    """Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < threshold for num in lst)


# Example usage
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. It uses the `all` function with a generator expression to check this condition. The example usage demonstrates how to use the function with the provided test cases.