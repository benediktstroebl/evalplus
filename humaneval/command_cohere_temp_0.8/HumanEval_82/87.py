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
    string = str(sum(map(ord, string)))
    # converting the sum to string to make sure it's treated as a decimal integer
    return is_prime(int(string))
```
This script defines a function 'prime_length' that takes a string value as an input and returns True if the length of the string is a prime number, and False otherwise. It achieves this by using the `is_prime` function, which checks whether a given number is prime or not. 

The `is_prime` function first handles special cases like num <= 1 and num <= 3, then performs a basic check for divisibility by 2 and 3. It then starts checking for primality starting from 5, incrementing by 6 each time to check for all non-prime candidates.

The `prime_length` function sums the ASCII values of the characters in the input string and converts the sum to an integer to pass to the `is_prime` function. This allows the primality of the length of the string to be checked. 

This approach has a time complexity of O(n) where n is the length of the input string, due to the summation of ASCII values and subsequent primality check. It assumes that the list of primes smaller than `10^6` is small enough to be practically stored in memory. If the range of candidates to check for primality is changed, it may require auxiliary data structures to store the primes, such as a list or a sieve algorithm.