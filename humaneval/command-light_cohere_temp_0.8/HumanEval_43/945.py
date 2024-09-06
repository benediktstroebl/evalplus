```python
def pairs_sum_to_zero(l):
    """
    Check if all the elements in the list sum to zero.
    """
    Each element in l is 0 (and there are no other non-zero elements) --> return True
    """
    return all(x == 0 for x in l)

def test_pairsum():
    """
    Test the function pairs_sum_to_zero with a few cases.
    """
    Test cases with different types of lists and ensure the function returns the expected results.

# Test cases
test_pairsum([1, 3, 5, 0]) # => False
test_pairsum([1, 3, -2, 1]) # => False
test_pairsum([1, 2, 3, 7]) # => False
test_pairsum([2, 4, -5, 3, 5, 7]) # => True
test_pairsum([1]) # => False
```
The script defines a function pairs_sum_to_zero that checks if all the elements in a list sum to zero. The test_pairsum function tests the expected behavior of the pairs_sum_to_zero function with a variety of test cases.