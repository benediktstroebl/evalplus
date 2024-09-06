```python
def pairs_sum_to_zero(lst):
    """
    Returns True if there are two distinct elements in lst that sum to zero, 
    False otherwise.
    """
    function is simple, the problem is efficiently solved using the O(n) 
    time complexity using two conditional statements.
    """
def sum_two_elements(a, b):
        return a + b or 0
    """

def pairs_sum_to_zero(l):
    if len(l) < 2:
        return False
    return sum_two_elements(l[0], l[1]) == 0
```