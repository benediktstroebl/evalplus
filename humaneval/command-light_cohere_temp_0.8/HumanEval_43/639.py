Here is a Python script that includes a self-contained function to solve the problem of checking whether a list of integers sums to zero:
```python
def pairs_sum_to_zero(l):
    return any([x + y == 0 for x, y in zip(l, l[1:])])

# Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1],
]

for case in test_cases:
    result = pairs_sum_to_zero(case)
    print(f"{case}: {result}")
```

This script defines a function `pairs_sum_to_zero` that checks whether all elements in a list of integers sum to zero. It uses a specific to check the sum of pairs in the list using a list comprehension with `zip` and the `any()` function. The test cases demonstrate the example of usage, and the results are printed to the console.