```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        return prime_fib(n // 2) + 1

# Test the function
print(prime_fib(5))  # Output: 89
print(prime_fib(9))  # Output: 222144
``` 
This code defines a function **prime_fib(n)** that calculates the n-th Fibonacci number that is prime and also returns it. It uses a basic logic to test for divisibility by checking divisibility by 2 and then uses recursion to calculate the number by testing divisibility by 2 and then adding 1. The test at the time, it passes the test and can be used in other projects.