```python
def triples_sum_to_zero(l):
    """
    function takes list of integers and returns True if there are three 
    distinct elements in the list that sum to zero, and False otherwise.
    """
    a input:
    l: list of integers
    """
    if sum(set(map(sum, l))) == 0:
        return True
    return False
```