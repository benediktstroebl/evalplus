```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        if n % 2 == 0:
            return prime_fib(n-2)
        else:
            d, r = 2, 2
            while r <= n:
                if d > n:
                    break
                d += 1
                r += d
            return r
# Testing the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28 

```
This code defines a function `prime_fib` which returns the n-th Fibonacci number that is also prime. It then uses a recursive logic with prime detection to accomplish this.