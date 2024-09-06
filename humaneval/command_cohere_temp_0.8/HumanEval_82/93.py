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
    # using the is_prime function to check if each length of the string is a prime number
    return is_prime(len(string))
```
This Python script defines a function `prime_length` that takes a string as an input and returns True if the length of the string is a prime number or False otherwise. It defines another function `is_prime` that efficiently checks if a given number is prime. The `prime_length` function then uses `is_prime` to check the primality of the length of the input string.

The given test cases pass with this implementation.