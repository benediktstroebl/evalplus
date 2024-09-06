```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
The solution is to find two elements with sum = 0 in the list of integers.
```

def test_pairsumsumtozero():
    """
    Unit tests for the pairs_sum_to_zero function.
    """
    test if the
    """[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        l = [1, 3, -2, 1]
        assert pairsumsumtozero(l) == False
        assert pairsumsumtozero([0]) == True
        assert pairsumsumtozero([-3, 2, -5]) == True
        l = [1, 2, 3, 7]
        assert pairsumsumtozero(l) == False
        l = [2, 4, -5, 3, 5, 7, 8, 9]
        assert pairsumsumtozero(l) == True

test_pairsumsumtozero()
```
The function test_pairsumsumtozero runs a series of tests for all possible inputs, and this function is designed to be used as a unit test for the pairs_sum_to_zero function.