### below_threshold Function
#### Checks if all numbers in a list are below a specified threshold

```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    numbers (list): A list of numbers to check.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```
In this script, the `below_threshold` function uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the specified threshold. If any number is not below the threshold, `all` will return `False`, and conversely, if all numbers are below the threshold, `all` will return `True`.