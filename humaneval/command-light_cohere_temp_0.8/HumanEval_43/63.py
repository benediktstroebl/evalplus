```python
def pairs_sum_to_zero(l):
    """
    checks if all elements in the list sum to zero.
    """
    return True if all numbers in the list add up to zero, and False otherwise.

# Tests
def test_pairsumtozero():
    """
    Test the pairsumtozero function
    """
    assert pairsumtozero([1, 3, -5, 4, 6]) == True
    assert pairsumtozero([1, 2, 3, 7]) == False
    assert pairsumtozero([0, 1, -3, -8]) == False
    assert pairsumtozero([2, 4, -5, 3, 5, 7]) == True

# Main code
if __name__ == "__main__":
    test_pairsumtozero()
```
This code defines a function `pairsumtozero` that checks whether all the elements in a list `l` add up to zero. The `test_pairsumtozero` function tests the `pairsumtozero` function with various input lists and asserts the results. The main code runs the test_pairsumtozero() to verify the correctness of the `pairsumtozero` function.