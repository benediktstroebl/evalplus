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

# Test Suite
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    return is_prime_length(string)

# Example usage
print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
```

This code defines a function `is_prime_length()` that checks whether the length of a given string is a prime number or not. 

Then it creates a test suite with the `prime_length()` function that uses `is_prime_length()` to test different strings to demonstrate its correctness.

The output of the code is:
```
True
True
True
False
```

Which corresponds to the examples given in the problem.