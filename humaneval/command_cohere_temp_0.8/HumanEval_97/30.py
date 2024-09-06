```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The code directly computes the product of the unit digits and then performs modulo by 10 to ensure the answer lies between 0 and 9, which is an integer. 

This solution is concise and directly leverages basic Python skills on the modular arithmetic and integer multiplication, which leads to a minimal codebase. 

It is also robust against potential future changes in the prompt specifications, such as nullifying the assumption of valid input.