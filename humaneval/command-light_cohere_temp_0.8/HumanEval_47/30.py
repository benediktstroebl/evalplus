```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
   
    # Get the median of the middle two elements in the sorted list
    m1, m2 = lst[-2:], tuple(lst[:-2])
    return float(m1 + m2) / 2
``` 
This Python function median sorts a list and then returns the median of the two middle elements. The function is self-contained, which means it can be used to solve the problem without relying on external functions or imports.