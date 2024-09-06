```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with different list types
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
print(max_element([]))
print(max_element([1, 2, 3, -100]))
print(max_element([True, False, True]))
print(max_element((10, 5)))
```