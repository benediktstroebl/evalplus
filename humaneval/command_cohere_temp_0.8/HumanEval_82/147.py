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

The `is_prime` function checks if a given number is prime. It first handles special cases for numbers less than or equal to 3, then checks if the number is divisible by 2 or 3, and finally uses trial division with odd numbers to check for primality. 

The `prime_length` function then uses `is_prime` to check if the length of the input string is a prime number, as requested by the problem.

The logic effectively checks if the string length is prime or not, returning True or False respectively, as exemplified in the original problem statement.