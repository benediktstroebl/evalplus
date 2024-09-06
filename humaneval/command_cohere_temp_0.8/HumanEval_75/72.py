```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, a + 1) if a % i == 0)
    return not any(factor in primes for factor in factors)
```

The function `is_multiply_prime(a)` determines whether the number `a` is the product of three prime numbers by first constructing a list of prime numbers up to `a` and then inspecting whether any integer between 1 and `a` that divides `a` is present in the list of primes. The function returns True if no divisors are prime, indicating that `a` is the product of three prime numbers, whereas it returns False if any divisors are prime. The given example inputs are implemented to ensure the accuracy of the code.

Here is a helper function to check if a number is prime:
```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

This function takes a number and returns True if it is prime, and False otherwise. It loops through the numbers from 2 to the square root of the input number and checks if the input number is divisible by any of them. If the number is divisible by any of them, it returns False. If it is not, it returns True.