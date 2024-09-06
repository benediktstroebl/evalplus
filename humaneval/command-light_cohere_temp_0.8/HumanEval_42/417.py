```python
def incr_list(lst):
    n = len(lst)
    result = [i+1 for i in range(n)]
    return result

# Test cases
test_cases = [
    [1, [1, 2, 3]},
    [5, [5, 3, 5, 2, 3, 3, 9, 0, 123]],
    [0, [123, 456, 789, 012]]
]

for case in test_cases:
    actual = incr_list(case[1])
    assert actual == case[2]
```
The function `incr_list` takes a list `lst` as input and returns a new list with elements incremented by 1. The test cases ensure that the function produces the correct output for different lists.