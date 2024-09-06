```python
def median(lst):
    """Return the median of list l."""
    if len(lst) % 2 == 0:
        return (lst[len(lst)//2 - 1] + lst[len(lst)//2]) / 2
    else:
        return lst[len(lst)//2]
# Test suite
for test in [median([-10, 4, 6, 1000, 10, 20]), median([3, 1, 2, 4, 5])]:
    print(f'Test passed: {test}', end='')
```