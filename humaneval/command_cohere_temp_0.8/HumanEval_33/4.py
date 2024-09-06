```python
def sort_third(l):
    l3 = [e for e in l if e%3 == 0]
    lX = [e for e in l if e%3 != 0]
    l3.sort()
    return lX + l3
```
This Python script defines a function `sort_third` which solves the problem as described in the prompt. It splits the input list `l` into two lists: `l3`, which collects elements that are divisible by three, and `lX`, which collects all other elements. After sorting `l3`, the function returns `lX` concatenated with `l3`, which yields the desired sorted list.