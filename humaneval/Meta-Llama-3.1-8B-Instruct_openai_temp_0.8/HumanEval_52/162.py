```python
def below_threshold(numbers: list, threshold: int):
    """Return True if all numbers in the list numbers are below threshold threshold.
    
    Args:
        numbers (list): A list of integers
        threshold (int): The threshold value
    
    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise
    """
    return all(num < threshold for num in numbers)

# Test cases
if below_threshold([1, 2, 4, 10], 100):
    print("Test case 1 passed")
if not below_threshold([1, 20, 4, 10], 5):
    print("Test case 2 passed")
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The function returns `True` if all numbers are below the threshold and `False` otherwise.

The script includes two test cases to verify the correctness of the function. If both test cases pass, it prints "Test case 1 passed" and "Test case 2 passed".