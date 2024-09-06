```python
def median(l: list):
    """Return median of elements in the list l.
    m = len(l)
    k = int(len(l) / 2)
    if m % 2 == 1:
        return (l[k] + l[k-1]) / 2
    else:
        return l[k]
median([-10, 4, 6, 1000, 10, 20]) # -> 15.0
``` 
This code defines a median function that takes a list of elements and returns the median value. The median is the average of the two middle numbers when the list has an odd number of elements, and it returns the middle number when the list has an even number of elements.