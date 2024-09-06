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
    # removing any non char bits and converting to utf-8 simplifies the problem
    string = remove_non_char(string)
    return is_prime(len(string))

def remove_non_char(string):
    return ''.join(char for char in string if char.isalpha())
```

This code defines a function `prime_length` that takes a string and returns True if the length of the string is a prime number, and False otherwise.

The `is_prime` function is used to determine if a given length is prime or not. Lastly, the `remove_non_char` function is used to remove any non-character elements from a string, simplifying the problem by ignoring meta-data about the string.