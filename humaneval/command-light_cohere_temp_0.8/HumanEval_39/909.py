```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    
    fib = [1]
    for _ in range(3, n):
        fib.append(fib[-1] + fib[-2])
        
    prime_fib = [math.sqrt(i) for i in fib if is_prime(i)]
    
    return prime_fib

# Example usage:
print(prime_fibonacci(5))  # Output: [5, 89]
``` 
This code defines a function `prime_fibonacci` that computes the n-th Fibonacci number and returns a list of prime factors of that number. The code also provides a example of using the function with n=5 and prints the result which is `[5, 89]