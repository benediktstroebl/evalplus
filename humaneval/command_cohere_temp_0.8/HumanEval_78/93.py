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

The algorithm consists of a list containing all the prime hexadecimal digits: `prime_hex = ['2', '3', '5', '7', 'B', 'D']`. Then the function `hex_key()` loops through each digit in the given `num` and checks if this digit is present in the `prime_hex` list, if true, it increases the counter `count` by 1. Finally, the function returns this count which represents the number of prime hexadecimal digits in the given `num`. 

Such a solution passes the test cases provided in the prompt and should do for other cases as well. 

Let me know if further clarification is needed or if there are other tasks we can assist with!