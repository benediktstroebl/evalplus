```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = [num for num in primes if n % num == 0]
    return len(divisors) == 3
```

The function `is_multiply_prime(n)` uses a list of known prime numbers to check if the given number is a multiplication of three of them. The function returns true if exactly three prime divisors are found and false if otherwise. You can enhance the function by adding other prime numbers to the `primes` list. The loop generates all divisors of the given number and checks if each one is present in the `primes` list, which contains all the prime numbers that can be multiplied to create the given number.