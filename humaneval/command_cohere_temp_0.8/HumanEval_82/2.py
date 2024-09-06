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
    if string == '0' or string == '1':
        return False
    return is_prime(string)
```

This script defines a function `prime_length` that takes a string and converts it to a numeric sum of ASCII values. It then determines if the length of the string is a prime number or not, finally returning True if it is, or False otherwise. This approach converts the string to a number and uses the `is_prime` function to determine if the length of the string is prime. 

The `is_prime` function is also included, which efficiently determines whether a given number is prime or not. It employs a combination of small prime number checks and divisibility rules to quickly rule out non-prime candidates. This optimized approach significantly reduces the number of iterations required to ascertain primality.