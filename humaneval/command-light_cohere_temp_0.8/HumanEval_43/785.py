```python
def pairs_sum_to_zero(l):
    return any([x + y <= 0 for x, y in zip(l, l[1:])])

# Tests
def test_pairsum():
    assert not_sum_to_zero([1, 3, 5, 0]) == False

def test_pairsum_2():
    assert not_sum_to_zero([1, 3, -2, 1]) == False

def test_pairsum_3():
    assert not_sum_to_zero([1, 2, 3, 7]) == False

def test_pairsum_4():
    assert not_sum_to_zero([2, 4, -5, 3, 5, 7]) == True

test_pairsum()
```
The script defines a function `pairs_sum_to_zero` that checks whether the sum of any pair of elements in the list is zero. The `test_pairsum` function contains several test cases to verify the correctness of the `pairs_sum_to_zero` function.