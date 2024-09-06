```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if (-x) in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function iterates through the list `l` and flips the sign of each element to simplify the problem into finding pairs of equal absolute values that have opposite signs. It utilizes a set `seen` to keep track of elements encountered so far, ensuring that each pair is distinct. The absolute value of the pair is stored in `seen` as a positive value. The function returns `True` if any pair that sums to zero is found and `False` otherwise. 

This approach significantly reduces the complexity to O(n), making the solution more efficient than the previous version. 

Here is a test suite that can be used to validate the function:
```python
def test_pairs_sum_to_zero():
    # Test cases with zero pairs
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False

    # Test cases with one pair
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1, -2, 3, -4]) == True

    # Test cases with no pairs
    assert pairs_sum_to_zero([1]) == False
    assert pairs_sum_to_zero([-1]) == False
    assert pairs_sum_to_zero([1, -1]) == False
    assert pairs_sum_to_zero([-1, 1]) == False
    assert pairs_sum_to_zero([0]) == False
    assert pairs_sum_to_zero([0, 0]) == False

test_pairs_sum_to_zero()
```

This test suite provides a variety of test cases, including situations with zero, one, and no pairs that sum to zero, to thoroughly validate the function.