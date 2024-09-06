```python
import re

def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prime_count = 0
    num_length = len(num)

    for digit in num:
        if digit in hex_digits:
            digit_as_int = int(digit) if digit.isdigit() else hex_digits.index(digit)
            if digit_as_int in primes:
                prime_count += 1

    return prime_count
```

This script contains a function called `hex_key` that solves the problem you described. It checks if each digit in the hexadecimal number is a prime number or not, and then counts the number of digits that are prime. The script assumes that the input is always correct or empty, and that symbols `A,B,C,D,E,F` are always uppercase.

The function uses a list of prime numbers (`primes`) and a list of hexadecimal digits (`hex_digits`). The `prime_count` variable is used to keep track of the number of prime digits encountered. The function iterates over each digit in the input number, checks if the digit is a hexadecimal digit, then checks if the digit (converted to integer) is in the list of prime numbers. If so, `prime_count` is incremented. Finally, the function returns the `prime_count`.

Note that the solution is not optimized for speed, as it iterates over the list of digits twice and creates a list of all digits for comparison, but it is concise and easy to understand.  If speed becomes an issue for large inputs, optimizing the solution is a worthwhile future improvement.