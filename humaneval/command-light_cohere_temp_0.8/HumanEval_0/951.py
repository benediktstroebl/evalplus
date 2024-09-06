Here is a self-contained Python function that checks if any two elements in a list are closer than a given threshold:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold
    """
    return any(x == y for x, y in zip(numbers, numbers[1:])) and numbers[1] <= threshold
```
This function uses a list comprehension and an equality check to determine if any two elements in the list are equal and if they are less than or equal to a given threshold. It returns True if any two elements are close to each other, otherwise False.