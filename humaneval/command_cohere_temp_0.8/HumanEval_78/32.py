```python
import math

def is_prime(n):
    """Check is n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # your code here
    count = 0
    digits = ['0','1','2','3','4','5','6','7','8','9', 'A', 'B', 'C', 'D', 'E', 'F']
    digits = [int(d) for d in digits]
    if isinstance(num, str) and num:
        for digit in num:
            if digits.index(digit) >= 0:
                if is_prime(digits[digits.index(digit)]):
                    count += 1
    return count
```

The solution algorithm is simple:
1. First, the function `is_prime` is imported from the module `math`. This function checks whether a given natural number is prime or not. A natural number is called prime if it is greater than 1 and cannot be written as a product of two smaller natural numbers.
2. The function `hex_key` counts the number of hexadecimal digits that are primes. It first defines an empty variable count and then lists the digits that can be encountered. Then, using the `index` method, the function searches for each digit in the list and if the digit is found, the function `is_prime` is called to determine whether the digit is a prime. The index of the digit is stored in the variable `digits.index(digit)` and this value is used to determine the corresponding digit in the list `digits`. Finally, the count variable is increased if the digit is prime.