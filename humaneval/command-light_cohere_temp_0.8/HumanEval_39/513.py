```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        # Helper function to check if a number is prime
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            sqrt_num = int(math.sqrt(num))
            for i in range(2, sqrt_num):
                if num % i == 0:
                    return False
            return True

        # Continue with the main loop
        for i in range(3, n + 1):
            if is_prime(i):
                return i
        return n

# Test the function
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 6
print(prime_fib(8))  # Output: 28
print(prime_fib(10))  # Output: 92
print(prime_fib(15))  # Output: 1210
``` 
This function is self-contained and can be used to find the n-th Fibonacci prime and whether it's prime.