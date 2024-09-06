```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        temp = prime_fib(integer_divisor(n))
        while integer_divisor(n):
            n //= integer_divisor(n)
        return temp + 1

def integer_divisor(n: int):
    for i in range(2, n + 1):
        if n % i == 0:
            return i
```
The function `prime_fib` returns the n-th Fibonacci number that is prime, and also it is also a Fibonacci number.