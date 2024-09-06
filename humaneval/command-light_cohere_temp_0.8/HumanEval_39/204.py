```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        a = prime_fib(n // 2)
        b = 2
        while b * b <= n:
            if prime_fib(b) == 0:
                break
            a = a * a + b
            b += 1
        return a
```
This function uses the technique of iterating through multiples of primes and stopping when a composite number is encountered, ultimately returning the first prime number encountered.