```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
        numbers (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)


# Test cases
if below_threshold([1, 2, 4, 10], 100):
    print("Test case 1 passed")
else:
    print("Test case 1 failed")

if not below_threshold([1, 20, 4, 10], 5):
    print("Test case 2 passed")
else:
    print("Test case 2 failed")
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the built-in `all` function with a generator expression to check each number in the list. The test cases at the end demonstrate the function's behavior with two different inputs.