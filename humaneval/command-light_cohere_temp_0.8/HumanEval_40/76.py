```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    True
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
        sum_of_elements = el
    return_true = False
        # Check if any three elements sum up to zero
    for i in range(len(l) - 2):
        temp = l[i] + l[i + 1] + l[i + 2]
        sum_of_elements = temp
        if sum_of_elements == 0:
            return_true = True
            break
    return return_true
```