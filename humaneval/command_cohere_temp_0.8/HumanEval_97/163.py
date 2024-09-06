```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers a and b as input, extracts the unit digits of both numbers using the modulo operation (`modulo 10`, which returns the last digit repeatedly), and then multiplies these unit digits. The result is again taken modulo 10 to ensure that the final answer is a single digit, which is then returned as the product of the unit digits. 

This solution adheres to the given assumption that the input is valid, and it handles cases like 'multiply(14, -15)'.