```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

#Test the function
assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
assertEqual(median([3, 1, 2, 4, 5]), 3)
assertEqual(median([10, 10, 10, 20, 20]) , 10.0)
```