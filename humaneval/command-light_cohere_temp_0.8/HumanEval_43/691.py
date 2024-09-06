Here is a Python script that includes a self-contained function with a test suite:
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test suite:
    >>> test_pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> test_pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> test_pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> test_pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> test_pairs_sum_to_zero([1])
    False
    """
    return False if not_sum_to_zero(l) else True

def not_sum_to_zero(list):
    return pairs_sum_to_zero(list)

# Run the function with test suite to verify if it is working correctly.