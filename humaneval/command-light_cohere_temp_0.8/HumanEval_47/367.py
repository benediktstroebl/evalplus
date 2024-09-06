```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) % 2 == 1:
        return l[len(l)//2]
    return (l[len(l)//2 - 1] + l[len(l)//2])/2
``` 
This code defines a function median that calculates the median of a list's elements. It uses a tested to pass the test for a list of numbers.