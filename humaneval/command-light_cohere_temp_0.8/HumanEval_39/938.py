Here's the solution to the problem using Python:
```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    if n % 2 == 0:
        return 4
    if n % 3 == 0:
        return 3
    temp = prime_fib(n // 3)
    if temp == 0:
        return temp
    return temp + 1
```
This code defines a function `prime_fib` that computes and returns the n-th Fibonacci number that is prime. It uses a time optimization by finding the number 3 (since it's a prime) if the number is divisible by 3, or if the number is 2 and it's prime, it returns 4.