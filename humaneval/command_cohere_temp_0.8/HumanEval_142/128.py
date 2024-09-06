```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
The function sums over the list, updating each list element value according to its index rules, and returns the total. 

You can verify the functionality with the following test cases:
```python
test_cases = [[1, 2, 3], [], [-1, -5, 2, -1, -5]]
expected_results = [6, 0, -126]

for t, r in zip(test_cases, expected_results):
    assert sum_squares(t) == r, 'Case ' + str(r) + ' failed for input:' + str(t)
```
The expected results are as described in the problem statement, and the test cases are designed to validate the function for various scenarios.