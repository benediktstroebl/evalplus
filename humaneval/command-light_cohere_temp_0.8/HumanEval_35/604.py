```python
def max_element(lst):
    return max(lst)

# Test the function with a variety of inputs
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([-2001, -500, -20]))  # Output: -500
print(max_element([10, 2, 4, 3, 8, 7] + [0]))  # Output: 10
print(max_element([[-1, 2, 0, 3], [4, 5, 6]]))  # Output: 0
```