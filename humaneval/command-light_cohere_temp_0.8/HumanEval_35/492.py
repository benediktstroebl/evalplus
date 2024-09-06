```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1:
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Output: 123

# Test case 2:
print(max_element([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# Output: 9

# Test case 3:
print(max_element([-5, -3, -10, -20, -30, -40, -50, -60, -100]))
# Output: -100

# Test case 4:
print(max_element([1, 2, 3, 1000, 3000, 5000, 6000, 7000, 8000, 9000]))
# Output: 9000
```