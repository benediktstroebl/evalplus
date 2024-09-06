Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ct, leftovers = 0, 0
    while need:
        if need >= rem:
            ct += rem
            need -= rem
        else:
            ct += need
            leftovers += need - rem
        rem = max(0, rem - need)
    return [ct, leftovers]
```

This function uses a while loop to repeatedly eat as many carrots as possible from the remaining stock, it starts by eating the maximum amount of carrots that can be obtained from the remaining stock `rem` and need, and it keeps track of the total carrots eaten `ct` and the remaining carrots `leftovers`. The loop continues until all the needed carrots have been eaten. Finally, it returns a list containing [total carrots eaten, remaining carrots].