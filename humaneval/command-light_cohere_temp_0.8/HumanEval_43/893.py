```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    test case:
    test_set = [1, 3, 5, 0]
    return sum(x+y for x,y in zip(test_set,test_set[1:]))==0
```