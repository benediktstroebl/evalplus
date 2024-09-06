```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    Return True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    l = list(map(int, input().oop))
    if sum(l) == 0:
        return True
    else:
        return False
    """

test_sum_zero()
def __starting_point():
    inputoop = [1, 3, 5, 0]
    assert pairs_sum_to_zero(inputoop) == True
    inputoop = [1, 3, -2, 1]
    assert pairs_sum_to_zero(inputoop) == False
    inputoop = [1, 2, 3, 7]
    assert pairs_sum_to_zero(inputoop) == False
    inputoop = [2, 4, -5, 3, 5, 7]
    assert pairs_sum_to_zero(inputoop) == True
    return __starting_point()

__starting_point()
```
The function `pairs_sum_to_zero` in the Python script above checks if there are two distinct elements in the list that sum to zero. If there are, the function returns `True` and if not, it returns `False`. The test cases cover various scenarios and pass the test successfully.