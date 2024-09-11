```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.

    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example usage:
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value. It uses the built-in `all` function along with a generator expression to check if all numbers in the list are less than the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The example usage section demonstrates the function with the given test cases.