```python
def triples_sum_to_zero(l):
    """
    function to find three distinct elements sum to zero in list
    """
    sum = 0
    for x in l:
        if sum > 0 and x != sum:
            sum += x
    return sum == 0
```