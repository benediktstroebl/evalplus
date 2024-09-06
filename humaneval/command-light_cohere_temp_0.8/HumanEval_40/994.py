```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """  
    set1 = []
    set2 = []
    for num in l:
        if (set1 and set2) and ((num not in set1) and (num not in set2)):  
            set1.append(num)
            set2.append(num)
   
        return False  
    if (set1 and set2) and ((sum(set1) + sum(set2)) == 0):  
        return True
    else:
        return False
```