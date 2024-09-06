Here's a Python function that checks if any two numbers in a list are closer than a given threshold:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    the given threshold
    """
    for x, y in zip(numbers, numbers[1:]):
        if math.abs(x - x + y) < threshold:
            return True
    return False
```
This function takes a list of numbers and a threshold as input, and returns True if any two numbers in the list are closer than the given threshold, False otherwise.