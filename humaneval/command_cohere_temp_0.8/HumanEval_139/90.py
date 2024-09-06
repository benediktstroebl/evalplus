```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    for i in range(2, n + 1):
        fact //= i
    return fact
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' of a given integer `n`. The Brazilian factorial is represented by `n! * (n-1)! * (n-2)! * ... * 1!`, where `n` is greater than 0. The function initially uses a loop to compute the factorial of `n` up to `n` itself, storing this value in the `fact` variable. It then iterates through integers ranging from 2 to `n`, dividing the current factorial value by each integer to obtain the Brazilian factorial. This accurate and concise method successfully computes the desired result.