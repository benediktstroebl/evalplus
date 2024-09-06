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

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning False if so. It then iterates from 2 up to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns False. However, if the number is not divisible by any number in this range, it returns True, indicating that the number is prime.

This approach is optimized because it only needs to check up to the square root of the number. Primes greater than 2 always have odd square roots, so it is guaranteed that if a number is composite, it must have a factor that is less than or equal to its square root.

Here is an example usage of the function:
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

This shows that the function is working correctly, returning True for prime numbers and False for non-prime numbers, corresponding to the specification in your original prompt.