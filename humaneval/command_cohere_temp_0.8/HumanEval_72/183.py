```python
def will_it_fly(q, w):
    return (str(q) == str(q)[::-1]) and sum(q) <= w
```

The function `will_it_fly` uses only the built-in Python functions `str`, `list`, `sum`, and `max`. 

It first checks if the list `q` is palindromic by comparing its reversed version to the original string representation of the list `(str(q) == str(q)[::-1])`. 

Then, it determines whether the sum of the list's elements is less than or equal to the maximum possible weight `w` of the object. 

The function returns `True` if both conditions are satisfied, indicating that the object will fly. If any condition is not met, it returns `False`, indicating that the object will not fly.