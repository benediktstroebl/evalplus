```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.

    Returns:
    bool: Whether all numbers in the list are below the threshold.
    """
    return all(num < threshold for num in lst)

# Example usage:
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks whether all numbers in the input list `lst` are below the given `threshold`. The function uses the built-in `all` function with a generator expression to check this condition. The example usage demonstrates how to call this function with different inputs.