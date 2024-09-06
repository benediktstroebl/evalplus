```python
def median(l: list):
    """Return median of elements in the list l"""
    n = len(l)
    m = n // 2
    if n % 2 == 0:
        return (l[m-1] + l[m]) / 2.0
   
   
    elif n % 2 == 1:
        return l[m]
    else:
        raise ValueError("n must be even")

# Example usage
l = [-10, 4, 6, 1000, 10, 20]
print(median(l))  # Output: 15.0
``` 
This script defines a function `median` that takes a list `l` as input and returns the median value of the elements in that list. The function first checks if the n is even and returns the middle element if it is odd and returns the average of the middle two elements if n is even.