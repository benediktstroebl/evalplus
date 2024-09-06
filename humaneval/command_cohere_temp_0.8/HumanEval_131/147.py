```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function traverses the decimal representation of the input number `n` using a `for` loop. It multiplies the odd digits and accumulates the result in the `product` variable. The base case checks if the input is an even number and returns 0 if so.