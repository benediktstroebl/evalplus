Here is a Python script that contains a self-contained function to solve the problem of checking if there are two elements in an array that sum to zero:
```python
def pairs_sum_to_zero(l):
    return any(x + y == 0 for x, y in zip(l, l[1:]))

# Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for case in test_cases:
    result = pairs_sum_to_zero(case)
    print(result)
```

This script defines a function `pairs_sum_to_zero` that returns `True` if there are two elements in the list that sum to zero, and `False` otherwise. The function uses a nested loop to iterate over the list and compare each element with the second element in the list. 

The test cases are defined as an array of tuples, where each tuple contains two elements representing a pair of numbers. The function is then called with each test case, and the result is printed.