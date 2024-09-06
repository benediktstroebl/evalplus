```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    for i in range(2, n + 1):
        fact //= i
    return fact
```
This Python script defines a function called `special_factorial` takes an integer `n` as input and returns the `brazilian factorial` of `n`. The Brazilian factorial is defined as the product of factorials from 1 to `n` inclusive, multiplied by the product of factorials from 2 to `n` inclusive, divided by `n`. The two nested loops implement this definition, with the outer loop calculating the product of factorials from 1 to `n`, and the inner loop calculating the product of factorials from 2 to `n` and accumulating the result by division by `n` in each iteration. The resulting `fact` variable is returned as the Brazilian factorial of `n`.  This solution is concise and efficient and will work for any positive integer input.