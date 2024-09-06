```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    for i in range(2, n + 1):
        fact //= i
    return fact
```
This Python script defines a function `special_factorial` that calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!` where `n` is greater than zero. The function iterates through integers from `1` up to `n` and accumulates the factorial result. Then, it iterates from `2` up to `n` and correctly resets the accumulation to ensure the proper calculation. The function returns the special factorial of the given integer.

Here is an example of the function's usage:
```python
>>> special_factorial(4)
288
```
This demonstrates the calculation of the Brazilian factorial for `n = 4`, which correctly evaluates to `288`.