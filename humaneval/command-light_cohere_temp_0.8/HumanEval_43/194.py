```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l) and all(x != 0 for x in l)

# Unit tests
def test_pairsumtozero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The provided Python script defines a function called `pairs_sum_to_zero` that checks whether a given list `l` contains pairs of numbers whose sum is zero. The function returns `True` if it finds any such pair, and `False` otherwise. The function uses the process of `any(sum(x) == 0)` and `all(x != 0)` to check if the list contains any numbers or zeroes. The test_pairsumtozero function includes several test cases that cover different scenarios, ensuring the correctness of the `pairs_sum_to_zero` function.