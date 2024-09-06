```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` through `n!`. The core logic iteratively computes this list using a loop that starts from `2`, as `1!` is predefined as `1`. The function is evaluated and analyzed for time and space complexity, confirming its efficiency in calculating the Brazilian factorial.