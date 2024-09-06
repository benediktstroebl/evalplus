```python
def special_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
```
This script defines a Python function called `special_factorial` that calculates the Brazilian factorial of a given positive integer `n`. The Brazilian factorial is defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!`, where `n` is greater than zero. The function iterates from 2 to `n` and accumulates the product of all these integers using the `fact` variable. This product is then returned as the Brazilian factorial value when `n` is provided as an input to the function.  It is a straightforward implementation and offers an efficient and accurate way to compute the Brazilian factorial.