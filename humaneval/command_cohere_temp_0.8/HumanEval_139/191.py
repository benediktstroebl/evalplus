```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```
This Python script defines a function called `special_factorial` which accepts a single argument `n`. This function calculates the 'special factorial' of n, which is defined as `n! * (n-1)! * (n-2)! * ... * 1!` where `n > 0`. The function achieves this by setting a variable `fact` to 1 and then iterating through values of `i` from 1 to `n` and updating `fact` by multiplying it by the current value of `i`. This way, the function computes the product of all positive integers from 1 to `n`, which is the desired 'special factorial'. The result is then returned as the output of the function. 

The script's purpose is to provide a concise and efficient way to compute the 'special factorial' of a given number `n` in accordance with the problem statement.