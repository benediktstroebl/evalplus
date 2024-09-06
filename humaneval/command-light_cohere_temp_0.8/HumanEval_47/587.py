```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
for test in [median([3, 1, 2, 4, 5]), median([-10, 4, 6, 1000, 10, 20])]:
    print(test, flush=True)
```