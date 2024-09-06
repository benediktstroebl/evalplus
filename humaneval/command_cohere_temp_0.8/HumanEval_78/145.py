```python
import math

def hex_key(num):
    prime_digits = ['2', '3', '5', '7', 'B', 'D', 'E', 'F']
    count = 0
    for digit in num.upper():
        if digit in prime_digits:
            count += 1
    return count
```

The algorithm works by first converting the input hexadecimal string `num` to uppercase to make comparison case-insensitive. It then iterates through each digit in the number and checks if the digit is one of the hexadecimal digits that are primes. The list of prime hexadecimal digits is stored in the `prime_digits` list. 

If a digit is found to be prime, it increments the count variable, which is used to count the total number of prime digits. After iterating through all digits, it returns the final count, which represents the number of prime hexadecimal digits present in the input number.

This algorithm has a time complexity of O(N), where N represents the number of digits in the input hexadecimal string, as it requires iterating through each digit once.