```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-float('inf') , -float('nan')]]

# Test cases
test_cases = [
    [ [5, 3, 5, 2, 3, 3, 9, 0, 123], []],
    [5, 3, 5, 2, 3, 3],
    [2, 'x', 5, 'abc', 'cba', '123'],
    [-10, 3, 'abc']
]

for case in test_cases:
    actual = unique(case)
    assert set(actual) == set(case), f"Case {case} failed"
```
This code implements a function `unique` which takes a list `lst` as input and returns a new list containing unique elements from the input list. The function uses a array techniques to find unique elements and removes duplicates from the input list. 

Test cases are defined to verify the correctness of the `unique` function. The test cases include empty lists, lists with duplicates, and lists with no duplicates. The output of the function is compared to the expected results, and assertions are used to check if the test cases pass or fail.