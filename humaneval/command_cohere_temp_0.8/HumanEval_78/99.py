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

The algorithm consists of a simple loop that goes through each digit in the passed hexadecimal number and checks if the digit is in the list of prime hexadecimal digits. The number of loops will be the count of prime digits. The list `prime_hex` contains all the prime hexadecimal digits. Such an approach allows us to pass the example tests provided above.