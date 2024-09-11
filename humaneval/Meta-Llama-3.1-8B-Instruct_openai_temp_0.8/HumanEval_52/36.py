### Solution
```markdown
### Below Threshold Function
#### Returns True if all numbers in the list are below the given threshold

```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list numbers are below threshold.
    
    Args:
        numbers (list): A list of numbers
        threshold (int): The threshold value
    
    Returns:
        bool: True if all numbers are below the threshold, False otherwise
    """
    return all(num < threshold for num in numbers)

# Example use cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input, and returns `True` if all numbers in the list are below the threshold. The `all` function in conjunction with a generator expression is used to check this condition. The example use cases demonstrate the function's usage.