```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 1
    is_prime = True
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        return n
```
The above code defines a function called `prime_fib` that computes the nth prime number by iterating through the prime numbers up to the square root of n and checking for divisibility.  It then computes the basic primality tests to determine if a number is prime or not, which is the correct approach.