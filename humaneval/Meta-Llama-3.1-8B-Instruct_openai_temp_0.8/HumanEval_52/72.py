```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example usage:
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
    print(below_threshold([1, 2, 3, 4, 5], 1))  # Expected output: False
```

In this script:

*   We define a function `below_threshold` that takes a list `lst` and a threshold `threshold` as arguments.
*   The function uses the built-in `all` function along with a generator expression to check if all numbers in the list are below the threshold.
*   The `all` function returns `True` if all elements in the given iterable are true, and `False` otherwise.
*   In the example usage section, we demonstrate how to use the `below_threshold` function with different inputs.