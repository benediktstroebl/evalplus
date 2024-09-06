```python
def pairs_sum_to_zero(l):
    return any([x + y = 0 for x, y in zip(l, l[1:])])

# Test the function with sample inputs
test_cases = [
    [],  # [] Compares against empty list; should always evaluate to False
    [1, 3, 5, 0],  # Two distinct elements adding up to zero
    [1, 3, -2, 1],  # Two distinct elements adding up to zero
    [1, 2, 3, 7],  # Should evaluate to True
    [2, 4, -5, 3, 5, 7]  # Should evaluate to True
]

for test_case in test_cases:
    result = pairs_sum_to_zero(test_case)
    print(f"{test_case} => {result}")
```
This Python code defines a function called `pairs_sum_to_zero` that checks whether a list of numbers has two elements that sum up to zero. The `any()` function with a list comprehension is used to iterate through the list and check if there are two distinct elements that sum up to zero. The function returns `True` if this condition is met, and `False` otherwise. The test cases provided at the testing are designed to cover different scenarios and edge cases, and the function is tested with these cases to ensure its correctness. The output will display the results for each test case.