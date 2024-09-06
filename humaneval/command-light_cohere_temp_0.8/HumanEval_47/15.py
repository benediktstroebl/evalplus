```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        return None  # No elements in the list
    middle = len(l) // 2
    if len(l) % 2 == 0:
        return (l[middle-1] + l[middle]) / 2
    else:
        return l[middle]
```  This code defines a function called median, which takes a list l as input and returns the median of its elements.  The function implements the median calculation using the approach: calculate the middle of the list and check if the length of the list is even or odd, then, respectively, return the average of the two middle elements or the middle element.