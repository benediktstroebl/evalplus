```python
def median(l: list):
    """Return median of elements in the list l"""
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2.0
   
    calculate_median(n)
    else:
        return l[n//2]
``` 
This code defines a function median that calculates and returns the median of a list of numbers. 
It handles the cases of even or odd-length lists, as required by the definition of median.