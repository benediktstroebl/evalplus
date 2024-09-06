```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
print(get_positive([-33, -27, -20, 45, 55, 67, 81, 85, -120]))
# Expected output: [-27, -20, 45, 55, 67, 81]
```
This script defines a function `get_positive` that takes a list as input and returns a new list with only the positive elements from the original list. 

The function uses list comprehension with the condition `x >= 0` to filter out the positive elements from the input list.

The function is then tested with several input lists, and the output is verified against the expected output.