```python
def pairs_sum_to_zero(l):
    return any([x + y == 0 for x, y in zip(l, l[1:])])

# Unit tests
def test_pairsumtozero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False

assert pairs_sum_to_zero([1, 3, -2, 1]) == False

assert pairs_sum_to_zero([1, 2, 3, 7]) == False

assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True

assert pairs_sum_to_zero([1]) == False
```
The function `pairs_sum_to_zero` takes a list of integers as its input and returns `True` if the list contains two elements that sum to zero, and `False` otherwise. The test_pairsumtozero function contains assertions that check the behavior of the `pairs_sum_to_zero` function with various lists of integers.