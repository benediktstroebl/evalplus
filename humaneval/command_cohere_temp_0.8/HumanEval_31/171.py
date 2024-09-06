Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function defines a logical sequence to determine if a given number is prime. It first checks if the number is less than 2, deeming primes as false. Next, it iterates through numbers from 2 to the square root of the input number, checking for divisibility. If the number is divisible by any iteration, it's not prime, and the function returns False. If the loop completes without finding a divisor, the number is prime, and the function returns True.

This approach leverages an optimized efficiency of O(sqrt(N)) by only requiring the loop to run up to the square root of the number. It's a tried and true method for prime checking. 

The unit tests provided in the original problem can be rewritten in Python as:
```python
# Testing the is_prime function
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

These tests cover a range of scenarios, confirming the function's operation for both prime and non-prime numbers.