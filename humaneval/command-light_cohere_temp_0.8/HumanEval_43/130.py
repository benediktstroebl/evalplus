```python
def pairs_sum_to_zero(l):
    """
    checks if there are two distinct elements in the list that sum to zero
    """
    return sum(x for x in l if x != l[-1] and x + l[-1] == 0) <= 1

#Test cases
test_sum_to_zero = [
    [True,   False, False, False, False],
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for x in test_sum_to_zero:
    got = pairs_sum_to_zero(x)
    assert got == x, "Test case: {}".format(x)

#Output:
```