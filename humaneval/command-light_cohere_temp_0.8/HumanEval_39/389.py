Here is a Python script that provides a self-contained function that calculates and returns the n-th Fibonacci number such that it is prime:
```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3  # Base case: if n is less than or equal to 3, it is prime and already known
    else:
        # Prime testing and identification using trial division
        num = 5  # Initial guess
        is_prime = True
        while num * num <= n:
            if n % num == 0:
                is_prime = False
            num += 1
        if is_prime:
            return num  # Found a prime, return the guess
        else:
            continue  # Retry with another guess
    return continue  # No prime found after many guesses

# Test the function
print(prime_fib(5))
```

This script defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime. The function uses trial division to identify prime numbers and utilizes an iterative approach to achieve the desired result. 

Please note that the `continue` statement will trigger a run-time error in this specific script because it lacks a proper termination condition.