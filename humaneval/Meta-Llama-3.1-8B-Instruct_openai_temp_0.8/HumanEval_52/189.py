```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(i < threshold for i in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

In this script, I've modified the function name to `below_threshold` for better readability, changed the variable names to make them more descriptive, and added a type hint for the `threshold` parameter. I've also added an example usage section at the end to demonstrate how to call the function.