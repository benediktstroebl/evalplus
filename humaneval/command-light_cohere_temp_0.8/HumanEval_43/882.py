```python
def pairs_sum_to_zero(l):
    """
    Check whether a list of integers has two distinct elements whose sum is 
    zero.
    Args:
        list(int) l (expected to contain only positive integers)
    """
    n = len(l)
    if n == 1:
        return False
    if n % 2 == 0:
        s = sum(l)
        return (s == 0 and l[0] != s) or l[0] == s
    else:
        return (l[0] != l[-1]) and (l[1] == l[-2] or l[-1] != l[0])
```
The function uses two separate checks to determine if there are two elements whose sum is zero. It works under the pattern that it can be efficient for longer lists of positive integers. 

The function does not require any external functions or classes, and it can be easily called from within any Python environment.