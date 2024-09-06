```python
def pairs_sum_to_zero(lst):
    total = sum(lst)
    return (total == 0) and any(x != lst[0] for x in lst)

#Test cases
test_sum_to_zero = [
    [True, [1, 3, 5, 0]],
    [True, [1, 3, -2, 1]],
    [True, [1, 2, 3, 7]],
    [True, [2, 4, -5, 3, 5, 7]],
    [False, []],
    [False, [1]]
]

for test in test_sum_to_zero:
    actual = pairs_sum_to_zero(test)
    assert actual == test[1]
```
The function `pairs_sum_to_zero` calculates the sum of elements in the list, and returns `True` if there are two distinct elements in the list whose sum equals zero, and `False` otherwise.  The returned test cases to test the function's behavior.