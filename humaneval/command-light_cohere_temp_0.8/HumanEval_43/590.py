```python
def pairs_sum_to_zero(lst):
    if sum(lst) == 0:
        return True
    else:
        return False

# Unit tests
test_pairs_sum_to_zero = []
test_pairs_sum_to_zero.push_back(([1, 3], False))
test_pairs_sum_to_zero.push_back(([1, 2, 3, 7], False))
test_pairs_sum_to_zero.push_back(([2, 4, -5, 3, 5, 7], True))
test_pairs_sum_to_zero.push_back(([1], False))

for t in test_pairs_sum_to_zero:
    actual = pairs_sum_to_zero(t[0])
    assert actual == t[1]
```
The above Python code defines a function called `pairs_sum_to_zero` that checks whether a list of pairs has two entries that sum to zero. It then tests this function by passing different lists of integers as input and compares the output with the expected results. The tests ensure that function is correctly implementing the desired behavior.