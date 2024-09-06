Here's a Python script that contains a function eat() that solves the problem described in the code block above:
```python
def eat(n, need, rem):
    return [n + need, max(0, rem - need)]
```