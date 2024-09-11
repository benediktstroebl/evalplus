```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold.
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Test cases
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Should print: True
    print(below_threshold([1, 20, 4, 10], 5))  # Should print: False
```

This script defines the `below_threshold` function, which uses Python's built-in `all` function in conjunction with a generator expression to check if all numbers in the list are below the threshold. The test cases are provided within the script and can be run to verify the function's correctness.