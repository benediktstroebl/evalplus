Here is a Python function that checks if any two numbers in a given list are closer to each other than a given threshold:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :param numbers: List[float] - list of numbers to check
    :param threshold: float - threshold value
    :return: bool
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False
```

The function works by iterating through the list of numbers and checking if there are any two numbers that are closer to each other than the given threshold. 

It then returns a boolean value that is True if any two numbers in the list are closer than the threshold, and False otherwise.