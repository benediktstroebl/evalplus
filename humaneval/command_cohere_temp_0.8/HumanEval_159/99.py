Here's a Python script that contains a function named `eat` which solves the given problem:
```python
def eat(n, need, rem):
    ate, leftover = n, rem
    if ate < need:
        ate += leftover
        leftover = 0
    return [ate, leftover]
```

This script defines a function `eat` that takes three parameters: `n` (number of carrots already eaten), `need` (number of carrots needed to be eaten), and `rem` (number of remaining carrots). The function attempts to satisfy the hunger of the rabbit by eating the required number of carrots. If there are not enough carrots remaining, it will eat all of the remaining carrots but still be hungry afterward. 

The function returns a list containing the total number of carrots eaten (`ate`) and the number of carrots left after the meals (`leftover`).