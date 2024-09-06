```python
def f(n):
    li = [0] * n
    for i in range(1, n+1):
        if i % 2 == 0:
            li[i-1] = factorial(i)
        else:
            li[i-1] = sum(range(1, i+1))
    return li

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
This Python script defines two functions. The first function, f, accepts an integer n as input and creates a list where each element corresponds to the result of a specific condition imposed on the index i: factorial of i if i is even, and sum of numbers from 1 to i if i is odd. The second function, factorial, computes the factorial of a given number n by iterating through all numbers from 1 to n, multiplying each by the running total, which starts at 1. This ensures that the result of f(5) is [1, 2, 6, 24, 15], as stated in the example.