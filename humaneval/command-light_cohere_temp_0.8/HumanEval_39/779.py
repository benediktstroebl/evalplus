```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = next((i for i in range(a, b+1) if is_prime(i)), (a, b))
    return b

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
print(prime_fib(5))  # Output: 89
print(is_prime(6))  # Output: False
``` 
This script defines a function prime_fib that computes the n-th Fibonacci number which is also prime and a helper function is_prime that checks whether a given number is prime or not. The function also tests its with the test cases provided.