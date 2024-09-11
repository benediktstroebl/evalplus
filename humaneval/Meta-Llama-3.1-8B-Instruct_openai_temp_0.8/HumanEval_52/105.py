### Solution

```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(i <= threshold for i in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

### Explanation

This script defines a function `below_threshold` that takes a list `lst` and a threshold `threshold` as input, and returns a boolean indicating whether all numbers in the list are below the threshold. The function uses the built-in `all` function in combination with a generator expression to check this condition. If any number in the list is not below the threshold, the `all` function will return `False`.