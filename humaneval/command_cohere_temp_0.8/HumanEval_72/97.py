```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the list `q` is both palindic (using the `== q[::-1]` check) and the sum of its elements is less than or equal to the specified maximum weight `w`. The reversed check ensures the list is symmetrical, and the sum check ensures the total weight stays within the flight capacity. If these conditions hold, it will return True; otherwise, it returns False.