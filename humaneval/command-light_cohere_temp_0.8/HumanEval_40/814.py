```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """

    list of integers should be passed as input.
    # Returns with three distinct elements that sum to zero
    # e.g. [1, 2, 3] + [4] - [5] = 0
    # => [1,2,3]
    # [3,4,5]
    # [6,7,8]
    # [9,10,11]
    # etc.
    s = 0
    # set of elements that sum to zero
    for num in l:
        if s and s <= num:
            s += num
    if s == 0:
        return True
    return False
```