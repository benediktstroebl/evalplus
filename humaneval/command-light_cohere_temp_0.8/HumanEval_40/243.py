```python
def triples_sum_to_zero(lst):
    """
    Returns True if there are three distinct elements in lst such that their sum is zero, 
    and False otherwise.
    """
    elements: list of integers
    """
    set1 = set()
    set2 = set()
    set3 = set()
    for num in lst:
        set1.add(num)
        set2.add(num)
        set3.add(num)
   
        return False
    if len(set1) == 3 and len(set2) == 2 and len(set3) == 1:
        return True
    return False
```