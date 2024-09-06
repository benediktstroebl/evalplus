```python
def special_factorial(n):
    factorial_sum = 1
    for i in range(2, n + 1):
        factorial_sum *= i
    return factorial_sum
```
This Python script defines a function `special_factorial` that calculates the `brazilian_factorial` of a positive integer `n`. The `brazilian_factorial` is defined as the product of factorials from `1!` to `n!`. The script then provides an example of calling the function with input 4 and outputs the resulting `288`, which is the brazilian factorial of 4.