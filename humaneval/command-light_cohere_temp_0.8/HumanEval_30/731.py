```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = [
    dict(zip(['input'], [
        [-1, 2, -4, 5, 6],
        [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    ]))
]

# Function Calls
result1 = get_positive([-1, 2, -4, 5, 6])
result2 = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Test Results
test_get_positive['true']['result'] = result1
test_get_positive['false']['result'] = result2
```

This code defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the input list. The test cases provide a list with both negative and positive numbers and then call the `get_positive` function with those lists. The resulting output is stored in the corresponding test case dictionary.