```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list of integers is not ordered, so we'll sort it first.
    return: False if input list has no elements that sum to zero, or there are not
        three distinct elements that sum to zero.
    """
sort_list(l)
    for i in range(0, len(l)-2):
        if l[i] + l[i+1] + l[i+2] == 0:
            return True
    return False
```