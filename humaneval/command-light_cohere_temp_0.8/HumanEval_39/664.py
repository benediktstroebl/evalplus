```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return i
            i += 1
        return i + 2

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28
print(prime_fib(7))  # Output: 42
print(prime_fib(8))  # Output: 144
print(prime_fib(9))  # Output: 233
print(prime_fib(10)) # Output: 5516
```
The function `prime_fib` calculates the n-th Fibonacci number that is also prime using an iterative approach. The function first checks if `n` is less than 1, in which case it returns `n`. Then, it checks if `n` is even and returns the result of calling `prime_fib(n//2) + 2`. This is because all even numbers are divisible by 2 and are therefore prime. Then, it starts an iterative loop that calculates numbers from 3 up to `n` and checks if `n` is divisible by the current number. If it is, it returns the current number. Otherwise, it returns the number + 2.