```python
def median(l: list):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
```
Here is a Python function `median()` which calculates the median of elements in the list `l` using different logic for even and odd number of elements.