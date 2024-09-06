```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    sum of the list of integers is defined as:
    sum(l)
    
    Return: True if there are three distinct elements in the list that sum to zero, 
    and False otherwise.

""" Tests:
    for el in l:
        sum_el = sum(l)
        if sum_el == 0:
            return False
    return True
```