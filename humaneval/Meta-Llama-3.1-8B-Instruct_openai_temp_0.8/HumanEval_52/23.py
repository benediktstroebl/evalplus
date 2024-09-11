```python
def below_threshold(lst: list, t: int) -> bool:
    """Return True if all numbers in the list lst are below threshold t.
    
    Args:
    lst (list): A list of numbers.
    t (int): The threshold value.
    
    Returns:
    bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(num < t for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list `lst` and a threshold value `t` as input. It uses a generator expression within the `all` function to check if all numbers in the list are below the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The example usage demonstrates how to call the function and print the results.