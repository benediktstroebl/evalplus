```python
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_length(string):
    string = str(string)
    # converting string to int to remove fiable factor '1' from string length
    return is_prime(int(string))
```
This code defines a function `is_prime(number)` that checks whether a given number is prime or not. It then applies this function to the length of the input string to determine if the string's length is prime. 

Here's how it works step-by-step:
1. The `is_prime` function takes a `number` as input and initially checks if the number is less than or equal to `1`, returning `False` in such cases as numbers less than or equal to `1` are not prime.
2. It further checks if the number is less than or equal to `3`. If so, it returns `True` as both `2` and `3` are prime.
3. For numbers greater than `3`, it employs the `Eratosthenes` sieve algorithm with the first few iterations:
    - It checks if the number is divisible by `2` or `3`. If so, it returns `False` as these numbers are not prime.
    - It then starts a loop from `i = 5`. At each iteration, `i` is incremented by `6` (skipping multiples of `2` and `3` as they are not prime).
    - Within the loop, it checks if the number is divisible by `i` or `i + 2`. If so, it returns `False` as it encounters a non-prime factor.
4. If the loop completes without finding any non-prime factors, the function returns `True`, indicating that the number is prime.

The `prime_length` function takes an input string and calls `is_prime` for the length of the string (converted to an integer to remove the factor of `1` from the string length). It then returns `True` if the length is prime and `False` otherwise.