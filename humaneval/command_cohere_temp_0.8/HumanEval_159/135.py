Here's a Python script that contains a function named `eat` that solves the given problem:
```python
def eat(n, need, rem):
    guts, leave = 0, 0
    while need:
        if need >= rem:
            guts += rem
            leave = 0
            break
        else:
            guts += need
            leave = rem - need
            need = 0
    return [guts, leave]
```
This script contains a function named `eat` that takes three parameters: `n` (number of carrots already eaten), `need` (number of carrots needed to eat), and `rem` (number of remaining carrots). The function sets up two variables, `guts` and `leave`, to keep track of how many carrots have been eaten and how many are left over, respectively. It then enters a while loop that continues as long as `need` is not equal to zero.

Within the loop, there are two conditional statements. The first checks if the `need` is greater than or equal to the `rem`. If so, it eats `rem` carrots, sets `leave` to zero, and breaks out of the loop. This is because if `need` is greater than `rem`, there are not enough carrots to satisfy the hunger, so the rabbit will eat all that is remaining and still be hungry. If the `need` is less than `rem`, it will eat exactly `need` carrots and set the `leave` equal to the difference between `rem` and `need`. Finally, the loop concludes with setting need equal to zero, regardless of which pathway was taken through the conditional statements.

The function finally returns a list of two elements, [guts, leave], which represent the total number of carrots eaten after meals and the number of carrots left after meals, respectively.

This solution works within the constraints laid out in the prompt, which includes that more extreme cases of eating more than 1000 carrots in a single sitting.