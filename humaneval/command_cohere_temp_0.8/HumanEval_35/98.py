```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```
The max_element function takes a list l as input and returns the maximum element in the list. The function uses the max function to compare and return the maximum value in the provided list. The behavior is demonstrated and tested with the provided example test cases.