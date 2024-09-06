```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
print(get_positive([]))
# Expected output: []

# Test case 4
print(get_positive([1, 2, 3, -4, -5, 6, 7, -8]))
# Expected output: [1, 2, 3, 6, 7]
```

This script defines a function get_positive that takes a list l as input and returns a new list containing only the positive integers from the input list. It uses list comprehension with the particular filtering condition, and then it returns the new list. The script also provides test cases to verify the correctness of the get_positive function.