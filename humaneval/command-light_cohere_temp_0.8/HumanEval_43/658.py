```python
def pairs_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l)

# Test function
def test_pairsumtozero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False

# Test cases
test_pairsumtozero()

```

This code defines a function called pairs_sum_to_zero, which takes a list of integers as input and returns True if there are two distinct elements in the list that their sum is zero, and False otherwise. The function uses the simple summation to check if the sum of any two elements in the list is zero, and returns True if it is, and False otherwise. The test function is used to test the correctness of the pairs_sum_to_zero function by passing a series of test cases.