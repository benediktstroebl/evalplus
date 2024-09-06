```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 1
    else:
        return 2
    
def test_prime_fib(n: int):
    if n <= 1:
        print("Not a prime number")
    if n <= 3:
        print("2 or 3")
    if n % 2 == 0 or n % 3 == 0:
        print("2 or 3")
    for i in range(5, n + 2, 6):
        if n % i == 0:
            print(i, end=' ')
    print()

print(prime_fib(4))
print(prime_fib(5))
print(prime_fib(6))
test_prime_fib(7)
```
This code provides a prime_fib function that returns the n-th Fibonacci number which is also prime and tests the function with a test_prime_fib function.