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

The function `prime_length` takes a string and returns True if the length of the string is a prime number or False otherwise. To accomplish this, the nested function `is_prime` is used to determine if a given number is prime. This function uses a combination of small numbers and modular division to quickly rule out non-prime candidates.

This code will correctly determine whether or not the length of a given string is a prime number.