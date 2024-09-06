```python
def median(l: list):
    """Return median of elements in the list l"""
    n = len(l)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
#test case 1
 assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
#test case 2
 assert median([-20, -10, 4, 6, 10]) == 5.0
#test case 3
 assert median([10, 20, 40, 30, 50]) == 35.0
```