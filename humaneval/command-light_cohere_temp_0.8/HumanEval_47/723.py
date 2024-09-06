```python
def median(l):
    """Return median of elements in the list l"""
    m = float('-inf')
    n = len(l)
    
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2.0
   
    general:
        return l[n//2]
        
    elif n % 2 == 1:
        return l[n//2]
    else:
        m = l[n//2]
        return m
```