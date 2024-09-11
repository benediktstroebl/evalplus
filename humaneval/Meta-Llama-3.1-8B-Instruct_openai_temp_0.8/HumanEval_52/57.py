```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below the threshold."""
    
    # Use the built-in all() function with a generator expression to check if all numbers are below the threshold
    return all(num < threshold for num in numbers)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold as input, and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the `all()` function with a generator expression to check this condition. The script then includes two test cases to demonstrate the function's behavior.