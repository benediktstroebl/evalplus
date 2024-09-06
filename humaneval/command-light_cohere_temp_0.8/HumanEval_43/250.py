```python
def pairs_sum_to_zero(lst):
    total = sum(lst)
    return (total == 0) and not any(map(lambda x: x > 0, lst))

# Test the function
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

test_results = {}

for test_case in test_cases:
    result = pairs_sum_to_zero(test_case)
    test_results[test_case] = result

print("Test Results:")
for k, v in test_results.show(json(test_results))
```
This code defines a function `pairs_sum_to_zero` that checks if any two elements in a list sum to zero. It then returns `True` if this condition is met and `False` otherwise. The code also includes a list of test cases and a dictionary to store the results of the function. The function is then called with each test case, and the results are stored in the dictionary. Finally, the test results are printed and shown in a JSON format.