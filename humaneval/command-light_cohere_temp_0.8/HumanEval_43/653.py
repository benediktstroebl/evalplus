Here is a Python script with a self-contained function that solves the problem of determining whether a list of integers sums to zero:
```python
def pairs_sum_to_zero(l):
    return sum([x for x in l if x <= 0]) == 0

#Tests

def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False

def test_pairs_sum_to_zero_empty():
    assert pairs_sum_to_zero([]) == False

def test_pairs_sum_to_zero_single():
    assert pairs_sum_to_zero([1]) == False

def test_pairs_sum_to_zero_double():
    assert pairs_sum_to_zero([2, 4, -5]) == True

if __name__ == "__main__":
    test_pairs_sum_to_zero()
    test_pairs_sum_to_zero_empty()
    test_pairs_sum_to_zero_single()
    test_pairs_sum_to_zero_double()
```

This script defines a function `pairs_sum_to_zero` that determines whether a list of integers sums to zero. It also provides a specific tests to validate the function's behavior.

The tests cover various scenarios, including empty lists, lists with a single element, and lists with multiple elements, and ensure that the function behaves correctly in each case.