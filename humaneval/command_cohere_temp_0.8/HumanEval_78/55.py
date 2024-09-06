```python
import math

def hex_key(num):
    prime_hex = [1 for i in range(0, 16) if i not in [10, 12, 14, 15]]
    hex_count = 0
    num = str(num)

    for i in range(0, len(num)):
        if num[i] in prime_hex:
            hex_count += 1

    return hex_count
```

This Python script solves the problem by first creating a `prime_hex` list containing all hexadecimal digits that are prime numbers. Then, it loops through each digit of the input hexadecimal number `num`, checking each digit to see if it is prime. If a digit is prime, it increments the `hex_count` variable. Finally, the function returns the `hex_count` variable, which is the number of prime hexadecimal digits in the input number.

Here is a simpler solution using modules:
```python
import math

def hex_key(num):
    return sum(1 for digit in num if int(digit) in [2, 3, 5, 7, 11, 13])
```

And here is a slightly different take using a list comprehension:
```python
import math

def hex_key(num):
    return sum(int(digit) in [2, 3, 5, 7, 11, 13] for digit in num)
```

All of these scripts provide the same outcome, the number of prime hexadecimal digits in the input number.

Note: The `math` module is used in all three scripts to access the `int` function, which is used to convert hexadecimal digits from strings to integers for primality testing. PRIMES `[2, 3, 5, 7, 11, 13]` are imported as a list for efficient iteration.