```python
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_length(string):
    string = str(string)
    # converting string to int to check if string length is a prime int
    # (e.g. 'abcdcba' -> 2, 'kittens -> 5, 'orange -> 4)
    return is_prime(len(string))
```

This script defines a function `prime_length` that takes a string as an input and returns `True` if the length of the string is a prime number and `False` otherwise. 

The `is_prime` function is utilized to check if a given number is prime. It employs the trial division method, testing potential divisors from 2 to the sqrt(n) to efficiently determine the primality of the number. 

The `prime_length` function first casts the string to an integer to ascertain its primality, and then utilizes the `is_prime` function to determine whether the length of the string is a prime number. 

This solution has a time complexity of O(sqrt(n)), making it an efficient approach for prime determination, particularly for larger numbers.