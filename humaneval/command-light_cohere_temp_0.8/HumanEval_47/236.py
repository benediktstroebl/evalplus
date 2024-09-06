```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test cases
for i in range(10):
    for j in [i + 1, i + 3]:
        if i < j:
            med = median([i, j, i + j])
            assert med == (i + j) / 2
```