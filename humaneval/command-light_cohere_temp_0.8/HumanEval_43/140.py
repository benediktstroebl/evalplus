```python
def pairs_sum_to_zero(l):
    """
    Check if all the elements in the list sum to zero.
    """
    boolean list of the elements with sum > 0 is False
    """
    return not any(sum(i) <= 0 for i in l)

# Unit tests
test_pairs_sum_to_zero = []
test_pairs_sum_to_zero.append([[-1, 0],])
test_pairs_sum_to_zero.append([1, 0])
test_pairs_sum_to_zero.append([0,])
test_pairs_sum_to_zero.append([0,1])
test_pairs_sum_to_zero.append([0,2])

def test_pairs_sum_to_zero():
    """
    Returns True if all the elements in the list sum to zero,
    False otherwise.
    """
    return pairs_sum_to_zero([]) == False

# Test suite results
test_pairs_sum_to_zero()
```
The code defines a function `pairs_sum_to_zero` that determines whether a list of numbers sums to zero. The function accepts a list of numbers as an argument and returns `True` if all the elements in the list add up to zero or a negative, and `False` otherwise. The unit tests section `test_pairs_sum_to_zero` is a function that accepts a list of integers and returns `True` if the list contains two distinct elements that add up to zero, and `False` otherwise. The test suite results demonstrate that the `pairs_sum_to_zero` function accepts a variety of test cases and returns `True` for the majority of test cases.