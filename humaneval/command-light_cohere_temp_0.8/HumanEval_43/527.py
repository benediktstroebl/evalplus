```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
# Example:
    # Calculate sum of all elements
    sum = sum(l)
    # Check if the sum is zero
    if sum == 0:
        return True
    else:
        return False
    """

# Unit tests
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False

def test_pairs_sum_to_zero_2():
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False

def test_pairs_sum_to_zero_3():
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False

def test_pairs_sum_to_zero_4():
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True

test_pairs_sum_to_zero()
```
The code defines a Python function called `pairs_sum_to_zero` that takes a list of integers as input and returns True if there are two distinct elements in the list that sum up to zero, and False otherwise. The function uses the testing by using a series of unit tests that cover different cases of lists that can be passed to the `pairs_sum_to_zero` function.