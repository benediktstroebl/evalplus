```python
def pairs_sum_to_zero(l):
    """
    Checks whether a list of integers has two sum to zero elements.
    Args:
        list(int or tuple)
    Returns:
        True if it has two such elements and False otherwise.
    """
    check
    two elements have the same sum to zero
    """
    return (hasattr(l, '__len__') and
            all(x+y<0 for x,y in zip(l,l[1:])))

def test_pairs_sum_to_zero():
    """
    Test the function pairs_sum_to_zero
    """
    assert pairs_sum_to_zero([1,3,5,0]) == False
    assert pairs_sum_to_zero([1,2,3,7]) == False
    assert pairs_sum_to_zero([2,4, -5, 3,5,7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The above code defines a function `pairs_sum_to_zero` that checks whether a given list of integers has two elements whose sum is equal to zero. The function uses the two-level nested zip with the list and its first element to compare the sum. The test_pairs_sum_to_zero function is used to test the `pairs_sum_to_zero` function.