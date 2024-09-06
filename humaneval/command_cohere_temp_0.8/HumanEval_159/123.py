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

This function uses a while loop that continues until either `need` or `rem` reaches zero. It adjusts the `ate` value to minimize the difference between `need` and `rem` and updates the leftovers accordingly. The final value of `ate` is added to the original eaten carrots (`n`), and the function returns a list containing the total number of carrots eaten and the number of leftover carrots.