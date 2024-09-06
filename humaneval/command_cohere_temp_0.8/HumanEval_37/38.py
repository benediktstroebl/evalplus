```python
def sort_even(l: list):
    even = [x for x in l if len(x) % 2 == 0]
    odd = [x for x in l if len(x) % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function `sort_even` that solves the problem as described in the prompt. It first identifies the even and odd indices using list comprehensions and then returns the odd values as they are while sorting the even values and returning them at the end. This ensures that the result maintains the original odd values and has sorted even values, as outlined in the problem statement.