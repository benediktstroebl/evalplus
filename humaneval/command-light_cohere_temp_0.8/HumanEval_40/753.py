```python
def triples_sum_to_zero(l: list):
    """
    Function to find three distinct elements in a list that sum to zero.
    Returns: True if there are three such distinct elements in the list that
    sum to zero, and False otherwise.
    """
    sum(map(lambda x: x, l)) >= 0
    return sum(map(lambda x: x, l)) >= 0
```