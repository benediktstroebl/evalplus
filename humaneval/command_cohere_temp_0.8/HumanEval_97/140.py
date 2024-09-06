```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The code directly computes the product of the unit digits of `a` and `b` and returns the result, without any explicit conversion of the digits to integers. This makes the code more concise and efficient, directly leveraging the modulo operation's characteristics. The `% 10` effectively extracts the last digit, ensuring the result remains within the range of 0 to 9, just as the unit digit should be. 

The result is promptly returned as the product of the unit digits, without any superfluous conversions or intermediate variables.