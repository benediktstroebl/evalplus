```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    for i in range(2, n + 1):
        fact //= i
    return fact
```
This Python script defines a function `special_factorial` that calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!` where `n` is greater than zero. The function iterates through integers from `1` up to `n` and calculates the factorial incrementally. It then iterates from `2` up to `n` and divides the accumulating factorial by each integer to get the correct result. 

Here is an example of an input and output of this function:
```
input = 4
output = 288
```