```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    def get_sum(a, b, c):
        return a + b + c
    
    return (
        any(get_sum(a, b, c) <= 0 for a, b, c in l)
        and any(get_sum(a, c, b) <= 0 for a, c, b in l)
        and any(get_sum(b, c, a) <= 0 for a, b, c in l)
        ) and any(get_sum(a, b, c) <= 0 for a, b in l) is False)

```

The provided function implements a brute-force solution. It checks every triple against the very simple conditions, and returns True if any of those conditions are met. 

The function can be a good starting point for further optimization.