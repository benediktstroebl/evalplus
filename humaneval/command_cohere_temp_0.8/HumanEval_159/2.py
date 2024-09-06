Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining
    elif need > 0:
        total = n + need
        remaining = 0
    return [total, remaining]
```

This function takes in three variables: `n` which is the number of carrots already eaten, `need` which is the number of carrots needed to be eaten, and `rem` which is the number of remaining carrots. The function returns a list containing two integers: the total number of carrots eaten after meals and the number of carrots left after meals. 

The function is designed to eat as many carrots as needed to fulfill the daily meal requirement, and subtracts that number from the total, or remaining if there are not enough carrots. The function will eat all the remaining carrots if they are less than the needed amount of carrots, but will leave the rabbit still hungry as there are no carrots left to eat. 

As the given constraints state, all the variables are constrained between 0 and 1000, and should not cause any errors while executing the function.