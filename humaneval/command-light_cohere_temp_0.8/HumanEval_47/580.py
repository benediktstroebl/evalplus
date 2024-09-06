```python
def median(l: list):
    n = len(l)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
median([3, 1, 2, 4, 5]) # 3
median([-10, 4, 6, 1000, 10, 20]) # 15.0
median([0, 2, 3, 4, 5]) # 2
median([1000, 2, 3, 4, 5]) # 3
```