```python
def median(l):
    """Return median of elements in the list l"""
    m = float('-inf')
    cnt = 0
    for x in l:
        if m < x:
            m = x
        cnt += 1
    if cnt % 2 == 1:
        return (m + x) / 2
    else:
        return m
#Test the function
 assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
 ```