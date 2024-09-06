```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("List must have at least two elements")
    return (l[len(l)//2] + l[len(l)//2 - 1]) / 2
``` 
This code defines a function `median` that takes a list `l` as input and returns the median of the elements in that list. 

The function first checks if the list has at least two elements, and if not, raises a `ValueError`. If the list has two elements, the function calculates the median by selecting the middle two elements and summing them. 

Finally, the function returns the median.