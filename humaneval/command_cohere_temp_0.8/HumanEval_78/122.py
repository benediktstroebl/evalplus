```python
import math

def hex_key(num):
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    count = 0
    for digit in num.upper():
        if digit in prime_list:
            count += 1
    return count
```

The code defines a function `hex_key` that takes a string `num` as input and counts the number of hexadecimal digits that are primes. The function first creates a list of prime numbers from 2 to 37 for a quick prime check. It then iterates through each digit in the hexadecimal number, checking each digit if it is a prime. If a digit is a prime, it increments the count variable. Finally, the function returns the count of prime digits.

Here is a more concise implementation using a more efficient prime checking function:
```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def hex_key(num):
    count = 0
    for digit in num.upper():
        if is_prime(int(digit)):
            count += 1
    return count
```
This implementation uses the more efficient `is_prime` function, which runs in logarithmic time.  This approach is faster and more memory efficient for larger inputs.