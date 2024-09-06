```python
def max_element(lst):
    return max(lst)

# Test the max_element function with some inputs
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123

# Test list type (list vs custom dict)
print(max_element([123, 2, 3])) # Output: 3
print(max_element([True, 2, 3])) # Error: ValueError: impossible to call ...
```