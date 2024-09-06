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
The max_element function uses the built-in max function to compare and return the highest value in the provided list l. This solution is concise and leverages Python's efficient built-ins to accomplish the task.