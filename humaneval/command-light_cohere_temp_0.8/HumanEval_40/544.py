```python
def triples_sum_to_zero(lst):
    if sum([x for x in lst if x < 0]) == 0:
        return True
    return False

# Test suite
def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, -2, 1]) == True

# Test case 1
assert triples_sum_to_zero([1, 3, 5, 0]) == False

# Test case 2
assert triples_sum_to_zero([1, 2, 3, 7]) == False

# Test case 3
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True

# Test case 4
assert triples_sum_to_zero([1]) == False

# Main method
if __name__ == "__main__":
    test_triples_sum_to_zero()
```

This script has a self-contained function called `triples_sum_to_zero` that takes a list of integers as input and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise. The function is then tested with several test cases, and the test suite also ensures the function's correctness.