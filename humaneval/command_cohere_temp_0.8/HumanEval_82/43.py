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

This script defines a function `prime_length` that takes a string and returns True if the length of the string is a prime number and False otherwise. It includes the `is_prime_length` helper function to simplify the prime checking for the string length. The function `is_prime_length` checks if the given length is less than or equal to 1, it returns False, if the length has any divisors between 2 and the square root of the length, it returns False, and if no divisors are found, it returns True indicating the length is prime. 

To use this function, you can call it with different strings to see whether their lengths are prime or not. 

This solution passes all the test cases provided in the prompt.