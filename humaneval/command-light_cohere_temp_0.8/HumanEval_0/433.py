Here is a self-contained Python function that checks if any two numbers in a given list are closer to each other than a given threshold:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(x != y for x, y in zip(numbers, numbers[1:])) and numbers <= threshold
```
This function uses the element comparison and list comprehension to check if any two numbers in the list are equal, and then uses the condition to return True if this is the case.

It also ensures that the numbers are smaller than the threshold to verify if the comparison is meaningful.