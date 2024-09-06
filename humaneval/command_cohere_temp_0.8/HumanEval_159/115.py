Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    if need > rem:
        eat_all = rem
        hunger = need - rem
    else:
        eat_all = need
        hunger = 0
    return [n + eat_all, hunger]
```
This script contains a function called `eat` which takes in three variables, `n` for the number of carrots already eaten, `need` for the number of carrots needed to be eaten, and `rem` for the number of remaining carrots. The script then returns a list with two items, the first being the total number of carrots eaten after eating the number of carrots needed, and the second being the number of carrots remaining after eating.

For example, if a rabbit had already eaten 5 carrots and needed to eat 6 more, but there were only 8 carrots remaining, the `eat` function would return `[11, 1]`.

This code snippet can be imported and used in other Python scripts to solve the given problem.