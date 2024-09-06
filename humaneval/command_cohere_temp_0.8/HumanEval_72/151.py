```python
def will_it_fly(q, w):
    return (len(q) == 1 or len(q) == 2 and q[0] == q[1]) and sum(q) <= w
```

The function will return True if the object will fly, and False otherwise. The condition for a balanced queue is `len(q) == 1 or len(q) == 2 and q[0] == q[1]`, and the condition for weight is `sum(q) <= w`.