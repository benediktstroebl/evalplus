```python
def median(lst):
    """Return the median of list l."""
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test cases
for _ in range(50):
    lst = [random.randint(0, 100) for _ in range(5)]
    print(median(lst), end=" ")
```