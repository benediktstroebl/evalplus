Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ate = n
    if need > rem:
        ate = rem
    self_hungry = need - ate
    return [ate, self_hungry]
```

The `eat` function takes in 3 variables: `n` for the number of carrots already eaten, `need` for the number of carrots needed to be eaten, and `rem` for the number of remaining carrots. With these three variables, the function eats the maximum amount of carrots it can from the remaining variable, and returns the number of carrots it ate and the number of carrots it still needs to eat to fulfill its meal. 

This code should work for the given examples and constraints provided, but feel free to ask if you'd like any adjustments.