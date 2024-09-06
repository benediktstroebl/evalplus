```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[n//2 - 1]) / 2
    else:
        return lst[n//2]

#Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4, 5]) == 4.0
assert median([0, 5, 4, 3, 6]) == 4.0
assert median([-2, -3, -1, -4]) == median([-4, -3, -2, -1])
```