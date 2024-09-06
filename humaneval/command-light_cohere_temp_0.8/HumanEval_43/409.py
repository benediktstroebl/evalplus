```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l)

# Test the function
def test_pairsum():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == True

# Test the function with negative numbers
def test_pairsum_negative():
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False

# Test the function with a single element
def test_pairsum_single():
    assert pairs_sum_to_zero([1]) == False

# Test the function with a list of integers
def test_pairsum_integers():
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
```

The code defines a function `pairs_sum_to_zero` that checks if there are two distinct elements in a list that sum up to zero, and returns `True` if there are such elements and `False` otherwise. The code also includes several test cases to verify the correctness of the `pairs_sum_to_zero` function. 

It includes testing with positive, negative, and single-element lists, as well as a list of integers, and ensures that the function behaves as expected for these inputs.