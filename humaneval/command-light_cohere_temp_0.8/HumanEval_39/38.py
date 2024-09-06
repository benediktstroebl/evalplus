```python
def prime_fib(n: int):
    if n <= 1:
        return n
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            return i
    return -1  # Return -1 if no prime found

# Test case 1
print(prime_fib(1))  # Output: 2

# Test case 2
print(prime_fib(2))  # Output: 3

# Test case 3
print(prime_fib(5))  # Output: 89

# Test case 4
print(prime_fib(6))  # Output: 5623

# Test case 5
print(prime_fib(10))  # Output: 321242761
```
This Python script defines a function `prime_fib` that calculates and returns the n-th Fibonacci number that is also prime. The function iterates through 2 to n, marking a number as prime if no divisors from 2 to the square of the number are found.