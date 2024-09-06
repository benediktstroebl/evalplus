```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        limit = 2**((n-4) // 2) + 2
        for num in range(4, limit+1, 2):
            if is_prime(num):
                return num
        else:
            return limit

def is_prime(num: int):
    if num <= 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

# Test the function
print(prime_fib(5))
print(prime_fib(6))
print(prime_fib(10))
```
This code provides a function `prime_fib` that computes the n-th Fibonacci prime number and checks if it's prime. It also provides a with a helper function `is_prime` that checks if a given number is prime.