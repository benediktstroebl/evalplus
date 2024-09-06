```python
def triples_sum_to_zero(l):
    """
    Function to check if list of integers can sum to zero.
    Returns: True if there are three distinct elements in the list that sum to zero, and False otherwise.
    """
    def check_sum(x, y, z):
        return x + y + z == 0
    return True if check_sum(x, y, z) and not len(set(l)) == 3 else False

triples_sum_to_zero = {**{'check_sum': check_sum, 'input': [list]} }
```