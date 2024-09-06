```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will correctly determine whether the object q will be able to fly through the given constraints. It returns True if the list q is both palindromic (balanced) and has a sum of elements that is less than or equal to the maximum possible weight w. Otherwise, it returns False. This generally implies that the heavier the object, the more balanced it needs to be to fly.