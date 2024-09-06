Here is a Python script that contains a self-contained function to solve the problem:
```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    set_list = []
    for num in l:
        if set_list != [] and num in set_list:
            return False
        set_list.append(num)
   
    return True
```

This script defines a function named `triples_sum_to_zero` that takes a list `l` of integers as input and returns `True` if there are three distinct elements in the list whose sum is equal to zero, and `False` otherwise. 

The function uses a set data structure to check if there are duplicate elements in the list.