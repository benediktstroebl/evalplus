Here's a Python script that contains a function eat() that solves the problem described in the code block:
```python
def eat(n, need, rem):
    return [n + min(need, rem), max(0, rem - need)]
```

This function takes in three variables: number (denoting the number of carrots already eaten), need (the number of carrots needed to be eaten), and remaining (the number of total remaining carrots). The function returns a list containing two numbers: the total number of carrots eaten after eating the number of carrots needed and the number of carrots remaining after eating the number of carrots needed. The function adheres to the constraints you provided in the code block and should handle any edge cases as well.