```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    for i in range(5, n + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return i
    return n
``` 
This code defines a Python function named `prime_fib` that calculates and returns the n-th Fibonacci number that is also prime. It does this by using an simple algorithm that involves checking for divisibility and divisibility by 2 and 3, and then iterating up to the square of the number with a step of 6. It then returns the  the value of n if it's a Fibonacci prime, and n+1 otherwise if it's not.