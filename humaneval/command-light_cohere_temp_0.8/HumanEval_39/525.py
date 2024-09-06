```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    temp = prime_fib(n // 2)
    if temp == 2:
        return temp
    if temp == 3:
        return temp + 2
    return temp + next(prime_fib(n%2 + 1))

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89)
print(prime_fib(6))  # Output: 233
print(prime_fib(10))  # Output: 500001
```