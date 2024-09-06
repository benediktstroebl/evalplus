```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3 (with complex numbers)
print(get_positive([1, 2, 3, -4, -5]))
# Expected output: [2, 3, 3]
```
This Python function `get_positive` takes a list `lst` as input and returns a new list with only the positive elements. This is use list comprehension to iterate through each element in the input list and filter out the positive numbers.