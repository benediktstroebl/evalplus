```python
def unique_digits(x):
    odd = [y for y in x if not any(int(c) % 2 == 0 for c in str(y))]
    return sorted(odd)
```

The condition `not any(int(c) % 2 == 0 for c in str(y))` efficiently assesses whether any digit of the number `y` is even. The list comprehension returns a list of all numbers in `x` that satisfy this condition. This list is then returned as the solution to the problem.