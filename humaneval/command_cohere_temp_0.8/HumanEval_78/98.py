```python
import math

def hex_key(num):
    prime_digits = {'0':0,'1':0,'2':1,'3':1,'4':0,'5':1,'6':0,'7':1,'8':0,'9':0,
                    'A':0,'B':1,'C':1,'D':2,'E':1,'F':0}
    return sum(prime_digits[d] for d in num if d in prime_digits)
```

The code defines a `hex_key` function that takes a hexadecimal number as input and counts the number of hexadecimal digits that are primes. The solution assumes that the input is always correct or empty, and symbols `A, B, C, D, E, F` are always uppercase. 

The dictionary `prime_digits` lists the digits 0-9 and A-F and assigns them the number of primes that match its decimal value. The function then iterates through each digit in the input number and adds the number of primes for each digit to the total count. The solution assumes that the input is well-formed and that all digits are valid hexadecimal digits. 

Note that the solution assumes the input is well-formed and that all digits are valid hexadecimal digits. Additionally, it assumes that the user is aware of the limited scope of the prime digits (2, 3, 5, 7, 11, 13, 17, 19, 23, and so on) and doesn't need to be alerted about it. However, if further user guidance is preferred, it could be added without detracting from the function's primary goal.