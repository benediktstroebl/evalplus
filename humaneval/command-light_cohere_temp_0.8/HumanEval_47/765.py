```python
def median(lst):
    # Sort the list
    lst.sort()
    
    # length = len(lst)
    middle = length // 2
    
    # If length is even, return the middle element
    if length % 2 == 0:
        return lst[middle]
    # If length is odd, return average of middle two elements
    else:
        return (lst[middle - 1] + lst[middle]) / 2
``` 
This script defines a function called median that calculates and returns the median of a given list. It does this using a simple sorting algorithm, and then determines whether the length is even or odd, and returns the appropriate median value accordingly.