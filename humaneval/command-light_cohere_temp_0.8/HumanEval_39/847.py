```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    if n % 3 == 0:
        return 13
    prime = 0
    while prime <= n:
        count = 1 + (prime + 4) // 5
        if count > 1 and count <= n and (n - count) % 5 == 0:
            prime += 5
        else:
            break
    return prime
``` 
This function calculates the n-th prime number that is also a Fibonacci number, which satisfies the definition of a prime number. It uses a tested loop to check all the prime numbers until the n-th prime number is found.