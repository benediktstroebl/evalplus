```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [5, 3]]

#Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [0, 2, 3, 5, 9, 123, 'abc'],
    [1, 2, 3, 4, 5, 'abc', 123]
]

for case in test_cases:
    assert unique(case) == [0, 2, 3, 5, 9, 123], "Test case failed: " + str(case)
```
This code defines a function `unique` that returns a list of unique elements in the input list `lst`. The function utilizes a set called `seen` to keep track of elements encountered, then iterates through the list, only adding elements not in `seen` and not the specified "numbers" (which are [5, 3] in this case) to the result list. The test cases section provides a list of input lists to `unique`, and it compares the output with the expected results.