Here is a self-contained Python function that solves the problem of checking if any two numbers in a list are closer than a given threshold:
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
This function has a function that returns True if any two numbers in the list are closer than the given threshold, and False otherwise. It uses two nested for loops to iterate over the list of numbers and checks if the difference between each pair of numbers is less than or equal to the given threshold.