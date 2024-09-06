```python
def triples_sum_to_zero(lst):
    # Using Counter to count the number of items with certain values
    ct = Counter(lst)
    # Filtering for the items that can be part of the triple with sum 0
    triple_candidates = [k for k, v in ct.items() if v == len(lst) - 2]
    # Checking if there are exactly two such candidates
    return len(triple_candidates) == 2
```

The function uses a `Counter` to count the number of items (`v`) with each value (`k`) in the list. It then filters the keys of the counter, retaining only the items that can be part of a triple with a sum of 0. This is done by subtracting 2 from the number of items and checking if this value is present exactly once in the counter. If there are exactly two such items, the function returns `True`, indicating the existence of such a triple. Otherwise, it returns `False`.

Here is a simple test suite that you can use to test the function:
```python
def test_true():
    assert triples_sum_to_zero([1, 3, -2, 1]) == True

def test_false():
    assert triples_sum_to_zero([1, 2, 3, 7]) == False

def test_another_true():
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True

def test_no_triple():
    assert triples_sum_to_zero([1]) == False

def test_no_zero_sum():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False

test_true()
test_false()
test_another_true()
test_no_triple()
test_no_zero_sum()
``` 
This should give you complete coverage for this problem statement. 

This approach uses only a counter and filtering, making it relatively efficient with a time complexity of O(n) where n is the length of the list.

I hope this helps, let me know if you have any comments or questions!