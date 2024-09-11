```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold.
    Args:
    lst (list): A list of numbers.
    threshold (int): The maximum allowed value.

    Returns:
    bool: True if all numbers are below threshold, False otherwise.

    Example:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < threshold for num in lst)


# Test the function
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Should print: True
    print(below_threshold([1, 20, 4, 10], 5))   # Should print: False
```

In this script, the `below_threshold` function uses the built-in `all` function and a generator expression to check if all numbers in the list are below the threshold. The `if __name__ == "__main__":` block at the end is used to test the function when the script is run directly.