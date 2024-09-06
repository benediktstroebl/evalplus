```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w == q[0] + q[-1] == sum(q[1:-1]) or len(q) == 1)
```

The function checks if the sum of elements in the list `q` is less than or equal to the given weight `w` and if the list is palindromic (balanced). The condition `w == q[0] + q[-1] == sum(q[1:-1])` checks if the list is palindromic, and the additional condition `len(q) == 1` checks if the list has only one element to avoid unnecessary computation, making the code more efficient.