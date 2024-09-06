```python
def max_element(l: list):
    """Return maximum element in the list
    >>> l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    >>> max_element(l)
    123
    """
    return max(l)

# test the function
l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(l))  # Output: 123
```
This Python script defines a function max_element that takes a list l as an argument and returns the maximum element in the list using the max() function. The script then tests the either a small list and an example with larger list.