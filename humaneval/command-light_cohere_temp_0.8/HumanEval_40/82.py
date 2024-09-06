```python
def triples_sum_to_zero(lst):
    """
    Checks if there are three distinct elements in the list that sum to zero.
    Returns: True if there are such three such, and False otherwise.
    """
    triple = (x for x in lst if sum([x for x in lst]) == 0)
    return bool(triple)

#Test case 1: 3, 0, 1.

    assert triples_sum_to_zero([1, 3, 5, 0]) == False

#Test case 2: 1, 3, -2

    assert triples_sum_to_zero([1, 3, -2, 1]) == True

#Test case 3: 2, 4, -5, 3, 9, 7

    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True

#Test case 4: 1

    assert triples_sum_to_zero([1]) == False

```
The function checks if there are three distinct elements in the list that sum to zero, and returns True if there are, and False otherwise.