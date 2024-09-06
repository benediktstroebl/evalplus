```python
def pairs_sum_to_zero(l):
    return any(x + y > 0 for x, y in zip(l, l[1:]))

# Tests
def test_pairsum():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False

def test_pairsum_neg():
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False

def test_pairsum_small():
    assert pairs_sum_to_zero([1]) == False

def test_pairsum_correct(intList):
    assert pairs_sum_to_zero(intList) == True

# Main function call
if __name__ == "__main__":
    test_pairsum()
    test_pairsum_neg()
    test_pairsum_small()
    test_pairsum_correct( [1, 3, 5, 9, 2, 7, -6])
```
The function `pairs_sum_to_zero` in the above code calculates the sum of two numbers from the list and checks if it's greater than 0. It returns `False` if there are two numbers that sum to zero, and `True` otherwise. The tests `test_pairsum` are functions that call `pairs_sum_to_zero` with different input lists and assert the returned value is correct. The main function then calls all the tests to ensure that the `pairs_sum_to_zero` function works correctly.