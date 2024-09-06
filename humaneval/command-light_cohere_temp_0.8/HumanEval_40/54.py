```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test suite"""
    assert sum([x for x in l if x < 0]) == 0, "List has at least one negative element"
    assert len([x for x in l if x < 0]) == 0, "List should have exactly three distinct elements"
    return True if sum([x for x in l if x < 0]) == 0 else False
 ```