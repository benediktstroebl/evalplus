Here's the code:

```python
def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    prime_fib_helper(n)

def prime_fib_helper(n):
    a, b = 2, 3
    for _ in range(n - 4):
        a, b = next(prime_seq) + b, a + b
    return a

# Sample prime sequence generator
def prime_seq():
    primes = [2, 3]
    while True:
        is_prime = True
        for num in primes:
            if num * 2 <= primes[0]:
                is_prime = False
        primes.append(num + num * 2)
        if is_prime:
            break
    return primes
```

You can use this code by calling the function with the desired value for `n`. You will get the n-th Fibonacci number that is also prime.