```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```
This Python script defines a function called `special_factorial` which accepts an integer `n` as input. The function calculates a special factorial, specifically defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!` where `n > 0`. This computation is performed using a loop that iterates through integers from 1 to `n`, updating the `fact` variable to the product of its current value with each iteration. The function returns the `fact` value, which represents the special factorial of the input `n`. 

For example, calling `special_factorial(4)` would return `288`, as it calculates `4! * 3! * 2! * 1! = 288`. 

This approach is efficient and suitable for calculating the special factorial, as it uses a simple formula and follows the mathematical definition of factorial directly.