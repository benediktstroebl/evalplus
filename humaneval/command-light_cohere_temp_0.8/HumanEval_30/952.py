```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test case 1
test_cases = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]]

for test_case in test_cases:
    print(get_positive(test_case))
    print("----")

# Test case 2
test_cases = [[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [1, 2, 3, 4, 5]]

for test_case in test_cases:
    print(get_positive(test_case))
    print("----")
```

The function get_positive receives a list as input and outputs a list that only includes the positive numbers from the input list. The test cases are examples that demonstrate how the function behaves.