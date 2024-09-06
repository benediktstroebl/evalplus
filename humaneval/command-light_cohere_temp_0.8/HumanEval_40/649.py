```python
def triples_sum_to_zero(l):
    """
    function to check if three distinct elements sum up to zero
    """
    return any(sum([x for x in set(l[i:i+1]]) == 0 for i in range(len(l)//2)))
```