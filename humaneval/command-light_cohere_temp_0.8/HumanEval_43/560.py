```python
def pairs_sum_to_zero(l):
    """
    Check if list of integers has two distinct elements whose sum is 
    zero.
    : Returns True if the05 if there are two such distinct elements, and False otherwise.
    """
    optimized using Binary Search on the list
    """
    lst = list(l)
    lst.sort()
    sorted(lst)
    for i in range(len(lst)//2):
        if lst[i] + lst[len(lst) - i - 1] == 0:
            return True
    return False
```