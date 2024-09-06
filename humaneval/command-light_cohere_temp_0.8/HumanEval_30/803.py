```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1: Positive numbers only
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

# Test case 2: Negative numbers only
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, -10]))
# Expected output: [5, 3, 9, 123]

# Test case 3: Mixed numbers and positives
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: [5, 3, 2, 3, 9, 123]
```
This code defines the function get_positive, which takes an input list lst and returns a new list with only the positive integers from the original list. It uses list comprehensions to filter and transform the input into the desired output.