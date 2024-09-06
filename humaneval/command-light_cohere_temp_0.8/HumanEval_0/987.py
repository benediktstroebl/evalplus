Here's a self-contained Python function that checks if any two elements in a list are closer than a given threshold:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```

This function returns True if any two elements in the list are closer than the given threshold, and False otherwise. The function uses two nested loops to iterate over all pairs of elements in the list and checks if their difference is less than or equal to the given threshold.