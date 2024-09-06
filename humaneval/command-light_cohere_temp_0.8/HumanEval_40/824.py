```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """

    input:
    l: list of integers
    """
    # Initialize variables
    sum = 0
    seen = set()
    for num in l:
        if sum + num > 0:
            sum += num
            seen.add num
       
            else:
            return False
    return True
```