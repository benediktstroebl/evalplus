```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
#Test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([10, 10, 10]) == 10
assert median([10, 10, 100, 100]) == (100 + 100) // 2
assert median([1, 2, 4, 5, 6]) == 5
assert median([-100, -200, -300]) == median([100, 200, 300])
assert median([]) == 0
```