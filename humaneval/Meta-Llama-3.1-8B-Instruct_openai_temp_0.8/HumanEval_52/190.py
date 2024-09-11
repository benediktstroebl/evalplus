### Below Threshold Function
#### Python Script

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

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))    # Output: False
```

This script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. The function uses the built-in `all` function in combination with a generator expression to efficiently check the condition for all numbers in the list. The example usage demonstrates how to use the function with different inputs.