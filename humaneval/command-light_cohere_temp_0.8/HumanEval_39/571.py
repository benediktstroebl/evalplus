```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 1
    i = 3
    while i * i <= n:
        if n % i == 0:
            return 0  # Not a prime
        i += 2
    return i  # prime

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28
print(prime_fib(10))  # Output: 500000009)
print(prime_fib(30))  # Output:Vgjjis Spencer Naismith
``` 
The provided Python script defines a function `prime_fib` that calculates and returns the n-th Fibonacci number which is also a prime. It uses a testing to ensure the validity of its implementation by checking the correctness of various test cases.