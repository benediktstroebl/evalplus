```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    else:
        # Calculate the sum of the first n prime numbers
        sum_primes = 0
        while n > 1:
            num = n + 2
            if is_prime(num):
                sum_primes += num
            n -= num
        return sum_primes

def is_prime(num: int):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    return num > 1 and all(num != i for i in range(2, num))

# Example usage
n = 6
result = prime_fib(n)
print("Prime Fibonacci Number:", result, end=" ")
print()
``` 
This code defines a function `prime_fib` that computes the n-th Fibonacci number which is also a prime, and another function `is_prime` that checks if a given number is prime or not. The code then demonstrates its function by computing the 6th prime Fibonacci number.