Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi = 0, 1
    while hi < len(l):
        if l[hi] < l[lo]:
            return False
        if l[hi] > l[lo]:
            hi += 1
        else:
            lo += 1
    return True
```

The function monotonic takes a list l as input and returns True if the elements of the list are monotonically increasing or decreasing. The function initially checks for the edge case when the list has one or zero elements and returns True in such cases. It uses two pointers, lo and hi, initially pointing to the first and second elements of the list, respectively. It traverses the list using the two pointers, comparing elements at these pointers. If the hi pointer encounters an element smaller than the lo pointer, the function returns False, as this violates the monotonicity condition. If the hi pointer encounters an element equal to the lo pointer, it simply moves to the next element. The lo pointer is also moved whenever the hi pointer is moved, ensuring that the two pointers are never pointing to elements that are equal. Finally, if the entire list is traversed without a violation, the function returns True, indicating that the list's elements are in a monotonic sequence.