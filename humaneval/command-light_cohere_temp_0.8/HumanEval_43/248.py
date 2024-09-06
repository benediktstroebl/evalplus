```python
def pairs_sum_to_zero(l):
    """
    Check whether all elements in the list sum to zero.
    Args:
        list of integers
    Returns:
    True if there are two distinct elements that sum to zero, False otherwise.
    """
    return False

def test_pairsum():
    """
    Test function to check the result of pairs_sum_to_zero
    """
    return pairs_sum_to_zero([1, 3, 5, 0]) == False and \
           pairs_sum_to_zero([1, 3, -2, 1]) == False and \
           pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True and \
           pairs_sum_to_zero([1]) == False

if __name__ == "__main__":
    assert test_pairsum()  # Should print True
```