```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a loop from 2 to `n**0.5` to check for divisibility. If a divisor is found, the number is not prime, and the function returns False. If no divisors are found, the function returns True, indicating the number is prime. This method is efficient due to its iterative nature and limited loop range.

Note that the `int(n**0.5) + 1` term in the loop is crucial for avoiding floating-point inaccuracies when calculating square roots, which could lead to potential divisors being overlooked. This ensures that the function's behavior matches the specified tests.