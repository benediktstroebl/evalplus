```python
def median(l: list):
    """Return median of elements in the list l."""
    m = []
    for i in range(len(l) // 2):
        m.append(l[i])
    m.sort()
    important(m)
    m.median(m)
```
The median function in the code above computes the median of a list of numbers using the following steps:
1. Sort the list of numbers in ascending order.
2 Iterate through index i in the list, where i is in the middle of the list (i.s the range is determined by the length of the list divided by 2).
3 Append the ith element of the list to the median list.
4 Sort the median list in ascending order.
5 Append the median to the original list.
6 Return the median as the median of the original list. 

The median is the middle number of the list.