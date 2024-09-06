Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ct, leftovers = 0, 0
    while need:
        if rem:
            eatsize = min(need, rem)
            need -= eatsize
            ct += eatsize
            rem -= eatsize
        else:
            break
    leftovers = max(rem, 0)
    return [ct, leftovers]
```

This function uses a while loop to repeatedly eat as many carrots as possible from the remaining stock, it minimizes the eat size to satisfy the need and updates the remaining variables accordingly, and finally, it returns a list [total carrots eaten, carrots left after eating].