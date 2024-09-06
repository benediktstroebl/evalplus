```python
def max_element(l: list):
    """Return maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return None
    max_el = max(l)
    return max_el
```
The code defines a function max_element which takes a list l as input and returns the maximum element in the list. Inside the function, it checks if the input list is empty, and if so, it returns None. Otherwise, it finds the maximum element using the max function and returns it.

The function includes a docstring that provides information about its purpose and behavior, and the unit tests in the docstring ensure that the function behaves correctly for different input scenarios. These tests confirm that the function returns the expected maximum element for both positive and negative integer lists.