```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 1
    if n % 3 == 0:
        return 3
    temp = prime_fib(n // 3)
    if temp == 0:
        return 0
    return temp + 2
``` 
This code defines a function `prime_fib` that calculates and returns the n-th Fibonacci number which is also prime. It employs an iterative approach, dividing the number into three parts and solving the problem with those parts recursively. The function also handles edge cases for small inputs and checks for divisibility by 2 and 3 to determine if the Fibonacci number is prime or not.