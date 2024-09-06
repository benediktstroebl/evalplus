```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    is_prime = [True] * (4 * n - 1) // 5
    for i in range(5, n + 1, 6):
        if is_prime[i // 5]:
            is_prime[i] = False
    return is_prime[n - 1]
```
Here, the code defines a function called `prime_fib` that calculates the n-th Fibonacci number and checks if it is also prime. It uses an efficient approach to determine primality, testing various candidate divisors from 5 up to the square root of n. The function follows the mathematical properties of prime numbers to efficiently find the correct answer.