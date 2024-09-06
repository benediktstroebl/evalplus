```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    function:
    input: l (list of integers)
    """
    # Initialize variables
    n = len(l)
    valid = True
    for i in range(n - 2):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] + l[j] + l[k] <= 0:
                    valid = False
                    break
    return valid
```