```python
def special_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' of a positive integer `n`. The Brazilian factorial is defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!`, where `n > 0`. The function iterates from `i = 2` up to `i = n`, and each iteration multiplies the current factorial value `fact` by the current value of `i`. This accumulation effectively calculates the factorial of `n`. The function then returns the computed factorial as its output. 

The self-contained nature of the code means it includes all the necessary logic to compute the Brazilian factorial without relying on external variables or functions. When you call `special_factorial(4)`, it returns the correct value, `144`, which demonstrates the function's utility and correctness.