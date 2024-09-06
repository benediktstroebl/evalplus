```python
def unique(lst):
    return list(set(lst))

# Test cases
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [10, 10, 20, 30],
    [],
    [10, 20, 30, 40, 50, 60],
]

for test_case in test_unique:
    assert unique(test_case) == [0, 2, 3, 5, 9, 123], f"Failed for {test_case}"
```
The provided code defines a function called `unique`, which returns a list of unique elements from a given input list. The test cases are defined to ensure that the `unique` function works correctly. 

It includes a series of test cases with different lists, and it uses assertions to check if the output of the `unique` function matches the expected unique elements.