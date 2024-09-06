```python
def triples_sum_to_zero(l: list):
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
    for el in l:
        if not_three_times_sum(el, l) == True:
            return False
    return True

def not_three_times_sum(el, l):
    """
    it returns True if the element and two other elements in the list sum to a number that is
    divisible by 3, and False otherwise.
    """
    for el1 and el2 in l:
        if el1 + el2 == 0 and el1 % 3 == 0 and el2 % 3 == 0:
            return True
    return False
```