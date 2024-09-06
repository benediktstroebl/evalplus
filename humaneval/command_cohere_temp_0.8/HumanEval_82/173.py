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
    string = str(sum(map(ord, string)))
    # converting the sum to string to make it a valid hex string
    # adding 1 to ensure numbers like '111' are not considered prime
    return is_prime(int(string, 16) + 1)
```

This script defines a function `prime_length` that takes a string and converts it to a base-16 sum of its characters' ASCII values. It then checks if this sum plus one is a prime number, returning `True` if it is and `False` otherwise. This algorithm aims to determine if the length of the input string has prime numbers as its factors, judging by its sum as a base-16 number plus one.

The `is_prime` helper function implements a basic primality test that checks if a number is divisible by 2 or 3, then iterates through numbers of the form 6k ± 1 up to the number's square root. If the number is divisible by any such number, it's not prime. If it passes all these tests, it's a prime number.