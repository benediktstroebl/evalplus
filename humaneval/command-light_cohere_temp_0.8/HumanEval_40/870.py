```python
def triples_sum_to_zero(l):
    """
    function to check if there are three distinct elements in the list that sum to zero
    """
    sums = []
    for x in l:
        sums.append(sum(x))
    return (sums==[0])
```