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

The algorithm works by using a list of hexadecimal digits that are prime numbers (`prime_hex`) to iterate through the input `num`, and incrementing a counter (`count`) each time a prime digit is found.

Here is a more detailed breakdown of the code:
- The library `math` is imported in order to have access to a variety of mathematical functions. 
- A list named `prime_hex` is created, which includes the prime hexadecimal digits ('2', '3', '5', '7', 'B', 'D').
- Initialization of a variable `count` to zero, which will be used to count the number of prime digits. 
- A `for` loop is used to iterate over each digit in the input `num`.
- For each digit, it checks if the digit is in the `prime_hex` list, which means it is a prime hexadecimal digit.
- If a prime digit is found, the `count` variable is incremented. 
- Finally, the function returns the count of prime hexadecimal digits. 

This approach allows the algorithm to efficiently determine the count of prime hexadecimal digits in the input number.