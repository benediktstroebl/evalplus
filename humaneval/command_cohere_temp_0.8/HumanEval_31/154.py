Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning false immediately if so. It then iterates from 2 up to the square root of the number `n`, checking if the number is divisible by any other number. If the number is divisible by any other number in this range, it returns false, indicating that the number is not prime. If the number is not divisible by any number in this range, it returns true, indicating that the number is prime. This algorithm is known as the `Sieve of Eratosthenes` which efficiently determines primality.

Here's an example of how you can use this function:
```python
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

This example provides further test cases to validate the functionality of the `is_prime` function based on the given problem statement.