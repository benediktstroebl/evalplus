```python
def pairs_sum_to_zero(lst):
    """
    Returns True if all elements in the list sum to zero, False otherwise.
    """
    two element in the list that their sum is zero
    for el in lst:
        if sum(filter(lambda x: x == el, lst)) == 0:
            return True
    return False
```
This function, `pairs_sum_to_zero`, takes a list `lst` as an argument and returns `True` if there are two elements in the list whose sum equals zero, and `False` otherwise. It achieves this by iterating through each element in the list, and checking if there exists an element in the list whose corresponding elements sum to zero.