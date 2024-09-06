Here is a self-contained Python script that defines a function called has_close_elements, that checks if any two elements in a list of numbers are closer than a given threshold.

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(abs(x - y) < threshold for x, y in zip(numbers))

# tests
test_passes = [
    [0.1, 0.0, 0.0, 0.0, 3.0, 2.8, 5.0, 0.0, 2.0], 0.3]
 #  ]
test_close_elements(test_passes, 0.0)
```
This script defines a function has_close_elements, which takes in a list of numbers and a threshold as input, and returns a boolean value indicating if any two elements in the list are closer than the given threshold. The function uses the Python's abs() function to find the absolute difference between each pair of elements in the list, and checks if this difference is less than the given threshold.