```python
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_length(string):
    string = str(string)
    # using the is_prime function to evaluate if each length of the string is prime
    return is_prime(len(string))
```

This script defines a function `prime_length` that takes a string as an input and returns True if the length of the string is a prime number and False otherwise. It uses the `is_prime` function to sequentially check divisibility for all numbers smaller than the length of the string.

The `is_prime` function is also included, which checks whether a given number is prime or not. It does this by iteratively checking divisibility for all numbers smaller than the given number. The function follows the efficient algorithm of checking divisibility only up to the square root of the number, iterating through progressively increasing odd numbers. 

This algorithm allows for more efficient primality testing, as checking divisibility for numbers larger than the square root increases the likelihood of a non-prime result. 

The logic used in this code is a simplified version of the Miller-Rabin primality test, which is a probabilistic algorithm for testing whether a given number is likely prime.