```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    return bool(sum( distinct_elements(l) ) == 0)

def distinct_elements(l: list):
    """
    distinct_elements takes a list as an input.
    It returns a a list of distinct elements in the list.
    """
    return set(l) - {set([])}

```