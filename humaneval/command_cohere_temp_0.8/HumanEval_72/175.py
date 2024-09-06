```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditions to determine if an object will fly:
1. The object is a list of at least two elements (`len(q) > 1`).
2. The sum of the list's elements does not exceed the maximum weight (`sum(q) <= w`).
3. The list is balanced (`q == q[::-1]`).

These conditions ensure that the object is a balanced list of weights whose sum is less than or equal to the maximum weight. The function returns `True` if all conditions are met to indicate that the object will fly. If any condition is not met, it returns `False` to indicate that the object will not fly.