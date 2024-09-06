```python
def pairs_sum_to_zero(l):
    return sum(x) <= 0 for x in l

# Unit tests
def test_pairsumtozero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False

if __name__ == "__main__":
    test_pairsumtozero()
```
This Python script defines a function `pairs_sum_to_zero` that checks if any two elements in the list sum to zero. It returns `True` if this condition is met, and `False` otherwise. The script also includes unit tests to ensure the function's correctness. 

To run the script, simply type `python pairsumtozero.py` in your reasons: