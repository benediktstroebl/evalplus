```python
import math

def hex_key(num):
    prime_hex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 0, 1, 3, 5, 7]
    count = 0

    for c in num:
        if c.isupper():
            count += prime_hex[int(c)]

    return count
```

The `hex_key` function takes a string num as input and counts the number of hexadecimal digits that are primes. The function first creates a list `prime_hex` that contains all hexadecimal digits and pre-computes which digits are prime for faster iteration. It then iterates through the provided hexadecimal number num and checks if each digit is uppercase, using the `isupper()` method. If the digit is uppercase, it converts it to a decimal number using `int(c)`, and with that decimal number, it checks whether that digit is prime, using the `prime_hex` list, and increments the count variable. Finally, the function returns the calculated count of prime hexadecimal digits. 

Note that the assumption is made that the input is always correct and that no edge cases, such as an empty string or incorrect hexadecimal digits, are not handled.  If those cases need to be considered, more error handling and input validation would be required.