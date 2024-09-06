```python
def is_prime_length(length):
    if length <= 1:
        return False
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return False
    return True

def prime_length(string):
    string_length = len(string)
    return is_prime_length(string_length)
```

This script defines a function 'prime_length' which takes a string and returns True if the length of the string is a prime number and False otherwise. It passes the given tests because:
- 'prime_length''Hello' returns True because the length of the string 'Hello' is 5, which is a prime number.
- 'prime_length'abcdcba' returns True because the length of the string 'abcdcba' is 7, which is a prime number.
- 'prime_length'kittens returns True because the length of the string 'kittens' is 7, which is a prime number.
- 'prime_length'orange' returns False because the length of the string 'orange' is 6, which is not a prime number (it has 2 and 3 as divisors).

The 'is_prime_length' helper function is used to determine if a given length is prime, using a streamlined optimization by checking only divisors up to the square root of the length. 

This approach significantly reduces the number of checks required, making the function more efficient for larger inputs.