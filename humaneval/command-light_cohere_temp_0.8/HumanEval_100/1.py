```python
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    return [i+1 for i in range(n+1)]

#Test cases
def test_make_a_pile():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(5) == [5, 7, 9, 11]
    assert make_a_pile(0) == []
    assert make_a_pile(6) == [6, 8, 10, 12]
```
This script defines a function `make_a_pile` that constructs a list representing a pile of stones with specified number of levels. It also includes a test cases that check the correctness of the `make_a_pile` function for different input values.