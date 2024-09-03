Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    tot, lef = n, rem
    if tot + need > rem:
        tot += rem
        lef = 0
    elif tot + need == rem:
        tot += need
        lef = 0
    else:
        tot += need
        lef = rem - (tot - n)
    return [tot, lef]
```

This function takes in three variables `n`, `need`, and `rem` as integers and returns a list containing two integers `[tot, lef]` where `tot` is the total number of eaten carrots after your meals and `lef` is the number of carrots left after your meals. The function updates the total and leftover calories based on the input and returns the final count. It also ensures that the constraints mentioned in the problem statement are followed. 

The code has a straightforward layout and solves the problem efficiently. It can be easily understood and is modular enough to accommodate future changes without compromising performance.