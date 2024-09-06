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
    # using the built-in method len to get the length of the string
    length = len(string)
    if is_prime(length):
        return True
    else:
        return False
```
This code defines a function `prime_length` that takes a string and returns True if the length of the string is a prime number and False otherwise. 

The `is_prime` function is used to determine if a given number is prime. This function checks whether the given number is less than or equal to 1, in which case it is not prime, or less than or equal to 3, in which case it is prime. If not, it checks whether the number is divisible by 2 or 3, in which case it is not prime. As these are the only prime integers less than or equal to the square root of the number, it then moves through integers of the form 6k ± 1, starting from 5, squared against the given number, to check whether the number is divisible by any of them. If the number is not divisible by any such integer, it is prime.

In the `prime_length` function, the string is first converted to an integer using `str(string)` and then passed to the `is_prime` function to determine if the length of the string is prime. 

This solution passes the test cases mentioned in the prompt:
```
prime_length('Hello') == True
prime_length('abcdcba') == True
prime_length('kittens') == True
prime_length('orange') == False
``` 
Therefore, this solution is correct.