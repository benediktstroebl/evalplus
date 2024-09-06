```python
def median(lst):
    """Return median of elements in the list lst."""
    return (sum(sorted(lst))+lst[len(lst)/2])/2 if len(lst)==len(set(lst)) else None
#tests
#print(median([-10, 4, 6, 1000, 10, 20]))
print(median([1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20, 30, 20]))
```