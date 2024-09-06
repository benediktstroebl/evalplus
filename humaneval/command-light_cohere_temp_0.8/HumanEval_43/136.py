Here is a Python script with a self-contained function that solves the problem of finding two elements in a list that sum to zero:
```python
def pairs_sum_to_zero(l):
    return any(x + y <= 0 for x, y in zip(l, l[1:]))

# Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1],
]

for test_case in test_cases:
    result = pairs_sum_to_zero(test_case)
    print(f"{test_case[0]} => {result}".format())
```
The function `pairs_sum_to_zero` takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The test cases are provided, and the function is evaluated for each case. The output will display whether the results is `True` or `False`.