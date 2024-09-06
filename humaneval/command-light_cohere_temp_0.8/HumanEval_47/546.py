```python
def median(l: list):
    """Return median of elements in the list l."""
    m = []
    for i in range(len(l)//2):
        m.append(l[i])
    return (m if len(m)==1 else median(l[m[1:] + l[:m[0]])) if len(m)>2 else float('?no'))

# Test cases
print(median([3, 1, 2, 4, 5])) # 3
print(median([-10, 4, 6, 1000, 10, 20])) # 15.0
print(median([1, 2, 3, 4, 5, 6])) # 3
print(median([10, 20, 30, 40, 30, 40])) # 30
print(median([10, 10, 10])) # 10
```