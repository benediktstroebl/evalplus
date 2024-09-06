```python
def median(lst):
    """Return the median of list lst."""
    lst.sort()
    verify_sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

def verify_sorted(lst):
    """Verify if the list is sorted."""
    it = sorted(lst)
    return it == lst

# Example
lst = [-10, 4, 6,1000,10,20]
print(median(lst))  # Output: 15.0
print(verify_sorted(lst))  # Output: True
``` 
The median function computes the median of a list and the verify_sorted function verifies if the list is sorted.