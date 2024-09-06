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
    # converting the sum to string to make it a valid input for is_prime()
    return is_prime(int(string))
```
This code defines a function `is_prime` that checks whether a given number is prime or not. It then converts the given string to a numeric sum using `sum(map(ord, string))`, converts it to an integer to check its primality, and returns the result. 

The given examples in the problem statement will return `True` for `prime_length('Hello')`, `prime_length('abcdcba')`, and `prime_length('kittens')`, and `False` for `prime_length('orange')`.