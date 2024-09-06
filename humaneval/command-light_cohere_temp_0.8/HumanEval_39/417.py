```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 1
    temp = prime_fib(n // 2)
    if temp == 2:
        return 3
    return temp + prime_fib(n % 2)

print(prime_fib(5))
``` 
This code defines a recursive function `prime_fib` that calculates the n-th Fibonacci number that is prime and returns it. The function uses a technique of dividing the problem into smaller subproblems and using recursion to solve them. 
This function is self-contained and does not require any additional functions or variables to be defined.