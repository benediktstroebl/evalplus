```python
import math

def hex_key(num):
    prime_hex = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in prime_hex:
            count += 1
    return count
```

The algorithm works by using a list of hexadecimal digits that are prime numbers (`prime_hex`). It iterates through each digit in the input number `num` and checks if the digit is in the `prime_hex` list. If it is, it increments the count variable. Finally, the function returns the count variable, which is the number of prime hexadecimal digits in the input number.

Here is a more concise version using Python's `itertools.filter` and `map` functions for a cleaner filtering approach:
```python
import math
import itertools

def hex_key(num):
    return sum(1 for digit in map(int, num) if digit in (2, 3, 5, 7, 11, 13) and math.isfinite(digit))
```