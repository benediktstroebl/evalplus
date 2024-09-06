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
    if string == '0':
        return False
    return is_prime(string)
```
This code defines a function 'prime_length' that takes a string and converts it to a numeric sum of ASCII values. It then checks if the length of the string is a prime number or not, following the logic of the provided description. 

The 'is_prime' function is utilized to check if a given number is prime. This function handles both odd and even prime numbers and iterates through potential divisors, efficiently ruling out multiples of these divisors. The 'prime_length' function first converts the string to a numeric value and checks if it's 0, immediately returning False if so. It then calls 'is_prime' to determine if the string length is prime.