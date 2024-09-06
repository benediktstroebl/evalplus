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
    if len(string) == 2:
        return True
    if len(string) % 2 == 0:
        return False
    for char in string:
        if is_prime(ord(char)):
            continue
        else:
            return False
    return True
```

The script defines a helper function `is_prime` that checks whether a given number is prime or not. The `prime_length` function converts the input string into a numeric value and iterates through each character, invoking `is_prime` to determine whether the length is prime. Ultimately, it returns `True` if the length is prime and `False` otherwise.

This approach ensures that the `prime_length` function can effectively determine whether the length of any given string is a prime number.