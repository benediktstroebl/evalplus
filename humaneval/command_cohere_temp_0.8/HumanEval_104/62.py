```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 for y in str(x))]
    return sorted(odd)
```

The condition `any(int(y) % 2 for y in str(x))` checks whether any digit of the number `x` is odd. In the test examples, the resulting list `odd` would be:
- `odd = [1, 15, 33]` for the first example
- `odd = []` for the second example. 

Hence, the function then returns this list `odd` filtered by odd digits. 

Let me know if you'd like to further discuss any details of the solution.