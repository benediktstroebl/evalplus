```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print("Test Case 1: ", end="")
get_positive([-1, 2, -4, 5, 6])
print()

# Test case 2
print("Test Case 2: ", end="")
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, -10])
print()

# Test case 3 (Large list)
print("Test Case 3: ", end="")
get_positive([1, 2, 3, 4, 5, 6, 7, 8, 9])
print()

# Test case 4 (Mixed negative and positive numbers)
print("Test Case 4: ", end="")
get_positive([-5, -2, 4, -3, 8, 1, 2, 7])
print()
```
This script defines the `get_positive` function, which takes a list as input and returns a new list containing only the positive elements from the original list.  It can be used as a foundation for solving similar problems in Markdown code blocks.