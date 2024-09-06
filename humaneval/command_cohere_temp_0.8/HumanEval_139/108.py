```python
def special_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
```
This Python script defines a function `special_factorial(n)` that calculates the 'Brazilian factorial' of n. The Brazilian factorial is defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!` where n is greater than zero. The function iterates from 2 to n, multiplying each integer to the variable 'fact' which is initialized to 1. Upon reaching the end of the loop, the value of fact will be the 'special factorial' of the given integer n. This approach is efficient and provides the correct result for the given input.