```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    n= len(l)
    if n < 3: return False
    for i in range(n):
        if l[i] < 0: return False
        sum_curr = 0
        for j in range(i + 1, n):
            sum_curr += l[j]
        if sum_curr < 0: return False
    return True
```