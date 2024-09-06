```python
import math

def hex_key(num):
    """
    Determine the number of hexadecimal digits that are primes.
    """
    # make sure the input is a string
    num = str(num)
    
    # initialize the counter of interesting digits
    count = 0
    
    # iterate through each digit in the hexadecimal number
    for digit in num:
        # check if the digit is in the correct range and is uppercase
        if digit.isupper() and digit in '0123456789ABCDEF':
            # check if the digit is a prime
            if is_prime(int(digit)):
                count += 1
    return count

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
assert hex_key("AB") == 1
assert hex_key("1077E") == 2
assert hex_key("ABED1A33") == 4
assert hex_key("123456789ABCDEF0") == 6
assert hex_key("2020") == 2
```
This code defines the `hex_key` function, which:
1. Converts the input to a string.
2. Initializes a counter to keep track of prime hexadecimal digits.
3. Iterates through each digit in the hexadecimal number.
4. Checks if the digit is in the correct range and is uppercase.
5. If the digit passes the conditions, it checks if it's a prime.
6. Increments the counter if it's a prime.
7. Returns the final count of prime hexadecimal digits.

The `is_prime` function is used to check if a given digit (decimal value) is a prime number. The function:
1. Checks if the input number is less than or equal to 1; if so, it returns False.
2. Iterates from 2 up to the square root of the number (inclusive).
3. If the number is divisible by any of these integers, it returns False.
4. If the loop completes without finding a divisor, it returns True.

The test cases are designed to validate the behavior of the `hex_key` function for different scenarios. Each test case asserts that the function returns the expected count of prime hexadecimal digits based on the provided input.

Note: The `is_prime` function uses a simple primality test that involves checking divisibility by all smaller integers up to the square root of the number. This is known as the `Sieve of Eratosthenes` method. While this approach works well for small numbers, it becomes inefficient for larger numbers due to its time complexity of O(n*log(log(n))). There are more efficient algorithms for prime checking, but they involve more complex computations. The method used here is straightforward and suitable for handling hexadecimal digits, which are typically limited to finite ranges.