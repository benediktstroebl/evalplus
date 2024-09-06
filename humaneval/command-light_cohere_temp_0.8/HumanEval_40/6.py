```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    example usage:
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # initialize sum of numbers
    sum_ = 0
    # initialize index
    i = 0
    # loop through the list
    for num in l:
        # update the sum
        sum_ += num
        # check if there are three distinct numbers that sum to zero
        if i == len(l) - 2 and sum_ == 0:
            return True
        i += 1
    return False
```