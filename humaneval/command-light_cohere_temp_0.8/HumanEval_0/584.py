Here is a self-contained Python function that solves the problem you have described:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    bare True
    because any other is in the list that are closer to each other than the given threshold.
    returns: bool
    """