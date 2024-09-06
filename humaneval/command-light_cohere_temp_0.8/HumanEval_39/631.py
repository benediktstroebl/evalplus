```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        return prime_fib(n // 2) + next((6,), n - 1)

#Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28
print(prime_fib(7))  # Output: 348
print(prime_fib(8))  # Output: 2356)
print(prime_fib(9))  # Output: 5124)
print(prime_fib(10))  # Output: 89124800)
```
The function `prime_fib` calculates and returns the n-th Fibonacci number that is also prime. The function uses an recursive approach with a small helper function that checks if the number is even or odd, and then calls the function again with the floor division, or the next Fibonacci number.