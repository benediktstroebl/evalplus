Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ate, leftover = 0, 0
    while need > 0 and rem > 0:
        ate += min(need, rem)
        need -= ate
        rem -= 1
        leftover += ate
    return [n + ate, leftover]
```

This function uses a while loop that continues until either `need` or `rem` reaches zero. Each iteration calculates the minimum between `need` and `rem` and adds that amount to both `ate` and `leftover`. The variables are then updated by subtracting `ate` from `need` and subtracting `1` from `rem`. The function finally returns a list containing `[n + ate, leftover]` which are the total number of carrots eaten after the meals and the number of leftover carrots respectively.

To use this code, you can add it to a Python file and run it. You can also import the function into another Python file where you might need to solve this specific problem.