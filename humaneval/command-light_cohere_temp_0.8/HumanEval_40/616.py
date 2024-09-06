```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    sum of all the triple = 0
    for i in range(len(l)):
        if l[i] != 0:
            sum_triple += l[i]
    if sum_triple != 0:
        return False
    return True
```