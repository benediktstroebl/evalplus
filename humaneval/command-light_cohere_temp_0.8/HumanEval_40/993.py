```python
def triples_sum_to_zero(l):
    """
    Returns True if there are three distinct elements in l such that their sum is zero, 
    otherwise False.
    """
    list comprehension is simple but takes advantage of Python's 
    built-in sum function.
    """
 triple_sum is sum(l[i] for i in range(3)) 
    """
    return False if sum(l) == 0 else True

# Test the function
test_ triples_sum_to_zero([1, 3, -2, 1], [2, 4, -5, 3, 9, 7]) 
```