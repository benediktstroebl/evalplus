```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    sum of all three elements = sum(x for x in l if len(set(x)) == 3)
    return not sum of three elements

test_ triples_sum_to_zero([1, 3, 5, 0])
test_ triples_sum_to_zero([1, 3, -2, 1])
test_ triples_sum_to_zero([1, 2, 3, 7])
test_ triples_sum_to_zero([2, 4, -5, 3, 9, 7])
test_ triples_sum_to_zero([1])
test_ triples_sum_to_zero([1, -2, 3, 4])
test_ triples_sum_to_zero([-1, 3, 4, 5])
test_ triples_sum_to_zero([]) # Empty list

```