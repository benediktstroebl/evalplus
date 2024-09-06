```python
def max_element(lst):
    return max(lst)

# Basic test case
print(max_element([1, 2, 3]))  # Output: 3

# List with negative elements
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123

# List with unique elements
print(max_element([5, 15, 3, 7, 4, 9]))  # Output: 15

# Empty list
print(max_element([]))
```