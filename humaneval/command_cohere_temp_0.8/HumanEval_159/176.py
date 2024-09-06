Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ct, leftovers = 0, n
    while need > 0:
        if leftovers == 0:
            return [ct, leftovers]
        ct += 1
        need -= 1
        leftovers -= 1
    return [ct, leftovers]
```

This function uses a while loop that continues eating until it reaches one of the following points:
1. It has eaten `need` carrots. At this point, it knows it has achieved its target and so returns.
2. It has eaten all the remaining carrots. In this case, it still returns as the rabbit is unable to eat any more, but is still hungry.

In both cases, it returns an array of two items `[total_eaten, leftover_carrots]`.