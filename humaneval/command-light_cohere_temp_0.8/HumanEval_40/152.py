```python
def triples_sum_to_zero(l):
    """
    Function to check if there are three distinct elements in a list that sum to zero.
    Returns: True if the three elements sum to zero, else False.
    """
    x = l[0]
    y = l[1]
    z = l[2]
    while x != y and x != z:
        if x + y == z:
            return False
        x = l[0] if x > y else y
        y = l[1] if y > z else z
    return True
```