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
    if len(string) <= 1:
        return False
    if is_prime(len(string)):
        return True
    return False
```

The `is_prime` function checks if a given number is prime. It first handles special cases for numbers less than or equal to 3, then uses a mixture of checks to iterate through potential divisors, ultimately returning True if no divisors are found. The `prime_length` function iterates through each length and uses the `is_prime` function to determine if the length is prime.

Here is a breakdown of how `prime_length` operates:
1. Length of a string is cleaned to be an integer using `str(string)`
2. A length of less than or equal to 1 is not prime, so it returns False
3. If the cleaned length is prime, it returns True
4. If the cleaned length is not prime, it returns False

This solution is robust and efficient, providing an accurate determination of whether a given string's length is a prime number.