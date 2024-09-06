```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    if n % 5 == 0:
        return 13
    prime_fib = n - 6
    return prime_fib

# Test cases
print(prime_fib(1))
print(prime_fib(2))
print(prime_fib(3))
print(prime_fib(4))
print(prime_fib(5))
print(prime_fib(6))
```
This function will return the n-th Fibonacci number that is also prime, where n is the argument passed. The function will check various conditions to determine if the number is prime or not, and then find the next prime number by subtracting 6 and return that.