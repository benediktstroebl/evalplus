```python
def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    for i in range(2, n + 1):
        result //= i
    return result
```
This Python script defines a function `special_factorial` that calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!` where `n` is greater than zero. The function iterates through integers from `1` up to `n`, calculating the factorial result using the `*` operator. Afterward, it iterates through integers from `2` up to `n`, dividing the result by the number to apply the proper definition of the Brazilian factorial. The final result is the calculated Brazilian factorial, handled gracefully with integers and Python operators.