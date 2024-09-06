Here is a Python script that implements the function `f` according to the problem statement:
```python
def f(n):
    ls = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ls.append(factorial(i))
        else:
            ls.append(sum(range(1, i+1)))
    return ls

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Tests:
print(f(5))
# [1, 2, 6, 24, 15]
```

This script defines a function `f` that returns a list based on the specification you provided. It also includes a nested function `factorial` to calculate the factorial of a given number `n`. The `print(f(5))` test line demonstrates the function's behavior for `n = 5`, correctly returning the intended list of values.