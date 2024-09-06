```python
def triples_sum_to_zero(l: list):
    """
    A function that checks whether there are three distinct elements in a list that sum to zero.
    It returns True if there is a solution, and False otherwise.
    """
    l: list
    return True  if sum(set(map(int, l)))) == 0 else False
```