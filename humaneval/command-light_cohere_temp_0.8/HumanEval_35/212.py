```python
def max_element(l: list):
    """Return maximum element in the list
    >>> l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    >>> max_element(l)
    123
    """
    return max(l)

# Test case 1
l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(l))  # Output: 123

# Test case 2
l = [5, 3, -5, 2, -3, 0, 0, 0, 1, -1]
print(max_element(l))  # Output: -1

# Test case 3
l = [5, 3, -5, 2, -3, 0, 0, 0, 0, 1]
print(max_element(l))  # Output: 5
```