```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3 (Negative list)
print(get_positive([-1,-2,-3,4,6]))
# Expected output: []
```
The function `get_positive` takes a list as input and returns a new list containing only the positive numbers from the input list. It utilizes list comprehension and filtering technique to achieve this.

This script is self-contained, and it can be used as a standalone function to solve the problem of getting only positive numbers from a given list.