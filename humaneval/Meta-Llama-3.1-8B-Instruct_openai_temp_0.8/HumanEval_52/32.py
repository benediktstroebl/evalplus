```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.

    Args:
        numbers (list): A list of integers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)


# Example usage:
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, the `below_threshold` function takes a list of numbers and a threshold value as input. It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements of the iterable are true, and `False` otherwise. The `if __name__ == "__main__":` block is used to demonstrate the function's usage.