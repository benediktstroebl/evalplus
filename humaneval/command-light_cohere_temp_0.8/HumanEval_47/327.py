```python
def median(l: list):
    """Return median of elements in the list l.
    def calculate_median(l):
        n = len(l)
        m = n//2
        return (l[m] + l[n-m-1]) / 2
    return calculate_median(l)

def calculate_median(l):
    if len(l) < 1:
        raise ValueError("List cannot be empty")
    if len(l) == 1:
        return l[0]
    mid = l[len(l)//2]
    left = l[len(l)//2 - 1]
    right = l[len(l)//2]
    return calculate_median((left, mid, right))

# Example
l = [-10, 4, 6, 1000, 10, 20]
print(median(l)) # Output: 15.0
```