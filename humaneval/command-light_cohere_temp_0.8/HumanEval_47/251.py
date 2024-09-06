```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2] + lst[n//2-1]) / 2
    else:
        return l[n//2]
#Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([-100, -200, -1000]) == -1000
assert median([]) == 0
assert median([12, 34, 12]) == 34
```