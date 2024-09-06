Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    val = n + need
    if val > rem:
        val = rem
    return [val, rem-val]
```

The function eats the maximum amount of carrots he can, assuming the total amount of carrots cannot exceed the remaining amount.