```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    l.sort()
    # Find the middle element
    mid = len(l) // 2
    if len(l) % 2 == 0:
        return l[mid]
    # If the list has an odd number of elements, return the middle element
    return l[mid - 1]
``` 
Ensure that the list is sorted beforehand since this function employs the median calculation method that involves finding the middle element. It then returns the middle element if the list has an odd number of elements. If the list has an even number of elements, the median is the average of the two middle elements.