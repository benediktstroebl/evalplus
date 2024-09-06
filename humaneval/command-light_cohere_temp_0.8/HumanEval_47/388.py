```python
def median(l):
    # Sort the list
    l.sort(l)
    
    # middle element calculation
    n = len(l)
    middle = n // 2
    
    # get the middle element
    m1 = l[middle - 1]
    m2 = l[middle]
    m3 = l[middle + 1]
    
    # return the median
    return (m1 + m2 + m3) / 3
``` 
This code defines a function called median that calculates and returns the median of a list of numbers. It does this by sorting the list and then calculating the middle element as (middle) of the sorted list, and then adding the middle elements. This ensures that the middle number is always an integer.