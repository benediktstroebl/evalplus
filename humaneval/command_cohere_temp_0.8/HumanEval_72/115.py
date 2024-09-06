```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the list `q` is both palindic (using the `== q[::-1]` condition) and its sum of elements is less than or equal to the maximum weight `w`. All examples provided in the prompt return the correct values using this function.