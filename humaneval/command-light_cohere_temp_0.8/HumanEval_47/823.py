```python
def median(l: list):
    """Return median of elements in the list l"""
    return (len(l) + 1) / 2 * (sum((i + 1) / 2 < l[i] < l[-1 - i] for i in range(len(l) - 1)))

# test cases
print(median([-10, 4, 6, 1000, 10, 20] )) # 15.0
print(median([10, 20, 100, 30, 40, 60])) # 40.0
print(median([1, 2, 3, 4, 5])) # 3.0
print(median([50, 5, 6, 7, 80])) # 50
```