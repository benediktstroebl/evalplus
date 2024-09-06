```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2] + lst[n//2-1]) / 2
    else:
        return lst[n//2]

# Test cases
for case in ['median([3, 1, 2, 4, 5])', '[-10, 4, 6, 1000, 10, 20]']:
    assert median(case) == case[0] # Should evaluate to same
```