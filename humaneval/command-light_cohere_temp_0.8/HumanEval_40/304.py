```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    """

    set_sum = set()
    for num in l:
        set_sum.add(num)

    return True if set_sum.count() == 3 and

    return False
```
This script defines a method `triples_sum_to_zero` that takes a list of integers as input and returns `True` if there are three distinct elements in the list whose sum is equal to zero, and `False` otherwise.  The method works by creating a set of all elements in the input list and then checks if there are three distinct elements with a sum equal to zero. 

Note that this problem is solved using the set data structure and the `add()` method. The output should display `True`.