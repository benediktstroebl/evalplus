```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in lst are below threshold, False otherwise.
    """
    return all(i < threshold for i in lst)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

This script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. It uses the built-in `all` function with a generator expression to efficiently check each number in the list. The example usage at the end demonstrates the function's behavior with two different test cases.