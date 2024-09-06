Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ate, leftover = 0, 0
    while need > 0 and rem > 0:
        leftover += 1
        ate += min(need, rem)
        need -= ate
        rem -= 1
    return [n + ate, leftover]
```

This function uses two while loops to solve the problem:
1. The first loop runs as long as `need` is greater than 0 or `rem` is greater than 0.
2. Inside the loop, it increases the `leftover` by 1 (since you're eating one carrot), then it adds to `ate` the minimum of `need` and `rem`. It removes either `need` or `rem` from the corresponding variable (depending on which is smaller). 

At the end, it returns a list with the total number of carrots eaten (`n + ate`) and the number of leftover carrots (`leftover`).