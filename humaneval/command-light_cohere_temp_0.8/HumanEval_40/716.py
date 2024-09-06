```python
def triples_sum_to_zero(lst):
    """
    function that returns True if there are three distinct elements in the list that sum to zero, and False otherwise
    """
    for i in range(3):
        total = lst[i] + lst[i + 1] + lst[i + 2]
        if total == 0:
            return True
    return False
```