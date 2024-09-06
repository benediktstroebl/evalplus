```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
median([3, 1, 2, 4, 5]) # 3.0
median([-10, 4, 6, 1000, 10, 20]) # 15.0
median([10, 10, 10]) # 10.0
median([1, 2, 3, 4, 5, 6]) # 4.0
median([10, -10, 10, -10]) # 10.0
median([10, 20, 30, 40]) # 30.0
median([1, 2, 4, 5, 6, 7]) # 5.0
```