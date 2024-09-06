```python
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    """
    if not isinstance(string, str):
        return False
    return is_prime(len(string))
```

This script defines a function `is_prime(num)` that checks whether a given number is prime or not. It employs a straightforward algorithm that iterates from 2 to the square root of the number and checks for divisibility. If the number is divisible by any integer within this range, it is not prime; otherwise, it is prime. This function is then used in the `prime_length(string)` function to determine whether the length of a string is a prime number. 

The `prime_length` function first checks if the input is a string and then proceeds to assess the length of the string using the `is_prime` function. This arrangement ensures that the `prime_length` function is self-contained and capable of efficiently determining the primality of string lengths, as evidenced by the fact that both functions work seamlessly with the provided test cases.