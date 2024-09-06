```python
def is_prime_length(input_str):
    string_length = len(input_str)
    is_prime = True

    if string_length < 2:
        return False

    for i in range(2, int(string_length**0.5) + 1):
        if string_length % i == 0:
            is_prime = False
            break

    return is_prime
```

This function `is_prime_length` takes a string as an input and returns True if the length of the string is a prime number or False otherwise. In the process of determining whether the length is prime, the function also accounts for edge cases where the length is less than 2 or is 0, returning False in both cases. It then checks for divisibility by numbers from 2 to the square root of the length, if any divisor is found, the length is not prime, if no divisor is found, the length is prime. 

The function could be improved further by adding more precise primality testing for larger numbers, but this basic approach would work well for the problem at hand. 

This solution should be able to pass all the tests cases as it is capable of determining whether a given string's length is prime or not, based on the provided examples.