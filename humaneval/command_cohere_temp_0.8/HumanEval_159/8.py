Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    return [n + min(need, rem), max(0, rem - need)]
```

This function takes three parameters, namely `n` which represents the number of carrots already eaten, `need` represents the number of carrots required, and `rem` represents the number of carrots that are remaining. The function returns a list containing two integers, which represent the total number of carrots eaten after meals and the number of carrots left after meals respectively.