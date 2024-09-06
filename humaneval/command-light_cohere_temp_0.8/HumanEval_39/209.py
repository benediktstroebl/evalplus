```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    else:
        # Check for prime factors recursively
        for i in range(0, 6):
            if n % i == 0:
                break
            else:
                n = n // i
        return n

# Test the function with given inputs
print(prime_fib(5))
``` 
This code is designed to calculate the n-th Fibonacci number that is also prime. It defines the function `prime_fib` that takes an integer `n` as input and returns the n-th Fibonacci number that is prime. The function uses an bottom-up approach to find prime factors and uses a 6-term trial division to check for divisibility. The output will be the number that passes all the tests.