```python
def median(lst):
    """Return the median of elements in the list lst.
    Return the median of the list elements, sorted in ascending order,
    and return the middle element.
    lst.sort()
   
        median(lst)
    """
    Ensure list is sorted
    med = sorted(lst)[len(lst)//2]
    return med

# Example:
median([-10, 4, 6, 1000, 10, 20])
# Output 15.0
```