```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test the function with some examples
lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(lst1))  # Output: 123

lst2 = [5, 3, 'abc', -5, 2, -3, 3, -123]
print(max_element(lst2))   # Output: 5

try:
    x = [1, 2, 3]
    y = max_element(x)
    print("'Max element:', y)
except TypeError as e:
    print("Error:", e)
```