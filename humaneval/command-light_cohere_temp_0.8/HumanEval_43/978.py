```python
def pairs_sum_to_zero(lst):
    return any([x+y == 0 for x, y in zip(lst, lst[1:])]) and not any([x+y != 0 for x, y in zip(lst, lst[1:])])

# Unit tests
def test_pairsumtozero():
    assert not_two_distinct_elements_are_sum_zero( [1, 3, 5, 0]) == False
    assert not_two_distinct_elements_are_sum_zero([1, 3, -2, 1]) == False
    assert not_two_distinct_elements_are_sum_zero([1, 2, 3, 7]) == False
    assert not_two_distinct_elements_are_sum_zero([2, 4, -5, 3, 5, 7]) == True
    assert not_two_distinct_elements_are_sum_zero([1]) == False

def not_two_distinct_elements_are_sum_zero(lst):
    return any([x+y == 0 for x, y in zip(lst, lst[1:])]) and not any([x+y != 0 for x, y in zip(lst, lst[1:])])
```