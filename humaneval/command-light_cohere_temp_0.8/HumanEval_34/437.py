```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float("inf")]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 6, 7],
    [2, "a", "a", 4],
    [float("inf"), -5],
    [5, 5],
]

for test_case in test_cases:
    assert unique(test_case) == sorted(set(test_case))
```
The function unique returns a list with unique elements from the input list lst, which are also sorted using the set() function. The test_cases variable contains a list of test cases, each containing a list of values. The function then iterates over each test case, and the value must be a unique element in the list and not equal to float("inf"). The sorted() function is used to sort the set of values, and the set of values must be equal to the original test case.