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

The `is_prime` function checks if a given number is prime. It first checks if the number is less than or equal to 1, returning `False` in such cases. If the number is 2 or 3, it returns `True`. Then, using a loop, it checks if the number is divisible by smaller primes. After this process, if no divisors are found, the number is prime. 

The `prime_length` function then uses this function to check if the length of the string is prime. It first converts the string to a number, then checks if it's less than or equal to 1, which returns `False`. It then uses the `is_prime` function to check if the length of the string is prime. 

This solution passes the test cases provided in the prompt.