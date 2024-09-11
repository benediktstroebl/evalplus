```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
    lst (list): A list of numbers
    threshold (int): The threshold to check against
    
    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise
    """
    # Use a generator expression to check each number in the list
    # The all function will return True if all numbers are below the threshold
    return all(num < threshold for num in lst)


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold as arguments. It uses a generator expression within the `all` function to check if all numbers in the list are below the threshold. The result is returned as a boolean value.