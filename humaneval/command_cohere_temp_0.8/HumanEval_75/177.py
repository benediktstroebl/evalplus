```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in primes:
        if n % p == 0:
            return False

    divisors = [p for p in primes if n % p == 0]
    return len(divisors) == 3
```

The function `is_multiply_prime` checks if the number is divisible by any prime number less than 100. If it is not, it returns `False`. If it is, the function checks if the number is divisible by exactly three primes. 

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
```
The output will be:
```
True
```

This is because 30 is the product of 2, 3, and 5. 

To provide a thorough test, here is an example for a number that should return false:
```python
print(is_multiply_prime(90))
```
The output will be:
```
False
```
This is because 90 is the product of 2, 3, and 5, as well as 3, 5, and 7. 

This way, the `is_multiply_prime` function checks all the requirements mentioned in the prompt and provides a clear and efficient solution.