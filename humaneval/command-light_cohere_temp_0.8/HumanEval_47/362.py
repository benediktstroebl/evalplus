```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```

The function median in this script accepts a list as an argument and determines the median value of the list's elements. The code then checks that the function satisfies the test cases that are supplied.