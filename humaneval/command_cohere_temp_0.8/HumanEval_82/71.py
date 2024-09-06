```python
def is_prime_length(length):
    if length <= 1:
        return False
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return False
    return True

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    return is_prime_length(len(string))
```

The function `is_prime_length` is a utility function that checks whether a given length is prime. This function is used by `prime_length` to evaluate whether the length of a given string is a prime number. The logic for determining prime numbers adapts the classic Sieve of Eratosthenes technique using a range loop that checks for divisibility. This approach is efficient due to its iterative nature, making it ideal for longer length checks. 

This code will provide accurate assessments of string lengths against the prime criterion stated in the problem statement.