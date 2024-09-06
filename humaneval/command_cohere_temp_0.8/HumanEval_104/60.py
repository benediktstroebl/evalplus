```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c % 2 != 0)) for i in x if int(''.join(c for c in str(i) if c % 2 != 0)) <= 999]
    return sorted(odd)
```
```notes
Make sure to take a closer look at the logic tests, especially the edge cases, to fully understand the problem.```