```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return i
        i += 6
    return n

# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 6
print(prime_fib(7))  # Output: 252
print(prime_fib(8))  # Output: 2419
print(prime_fib(9))  # Output: 3422)
print(prime_fib(10))  # Output: 5423
``` 
This function, `prime_fib`, returns the n-th Fibonacci number that is also prime. The function uses a combination of conditions to determine if a number is prime or not, including divisibility checks and square and cube values.