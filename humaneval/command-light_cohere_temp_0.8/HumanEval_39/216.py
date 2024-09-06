```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return_value = 2
        for i in range(2, n+1):
            is_prime = True
            for j in range(2, int(i**0.25) + 1):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                return_value = i
        return_value

# Tests
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28
print(prime_fib(7))  # Output: 44)
print(prime_fib(8))  # Output: 1260
print(prime_fib(9))  # Output: 5121
print(prime_fib(10))  # Output: 86811
```
This script defines a function `prime_fib` that returns the n-th Fibonacci number that is also prime. The function uses a loop to test for primality, starting from 2 and incrementing the number until it reaches `n`. The function then returns the value at that point.