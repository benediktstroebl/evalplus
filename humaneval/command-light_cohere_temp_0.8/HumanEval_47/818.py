```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]
#Test case 1
assert median([3, 1, 2, 4, 5]) == 3
#Test case 2
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
#Test case 3
assert median([1000, -1000, 1, 2, 3]) == 2
#Test case 4
assert median([1, 2, 4, 4, 5]) == 4
```