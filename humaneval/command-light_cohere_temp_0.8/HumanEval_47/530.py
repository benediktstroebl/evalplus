```python
def median(l: list):
    n = len(l)
    m = n // 2 + 1
    if n % 2 == 1:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]

# Test the function with a sample list
assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
```