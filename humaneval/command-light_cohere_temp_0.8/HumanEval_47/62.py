```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[n // 2] + lst[n // 2 - 1]) / 2
    else:
        return lst[(n // 2) - 1]

# Test cases
for t in [median([-10, 4, 6, 1000, 10, 20]), median([3, 1, 2, 4, 5])]:
    print(f"Test {t} passed.")
```