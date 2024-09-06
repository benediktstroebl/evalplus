```python
def triples_sum_to_zero(l: list):
    return any(sum(x) == 0 for x in l) and any(x != 0 for x in l)
def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
    assert len(set([x for x in test_data] - [0])) == 0

test_data = [1, 3, 5, 0]
test_data.py
 ```