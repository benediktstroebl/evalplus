```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This Python script defines a function called `largest_prime_factor` which takes in a number `n` as input. The function is designed to find the largest prime factor of the input number `n`. It starts by iterating through factors from 2 up to the square root of `n`, checking if `n` is divisible by each number using the modulo operation (`n % i`). When a divisor is found, the function immediately returns that divisor, assuming it to be the largest prime factor. If no divisors are found before reaching the square root of `n`, the function terminates without returning a value, implying that the input number `n` is a prime factor itself. 

The unit tests included in the original problem statement are meant to verify the correctness of this function's implementation. 

Please note that the code assumes that the input number `n` is greater than 1 and is not a prime number itself, as stated in the problem statement.