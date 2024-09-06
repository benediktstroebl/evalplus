```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits to obtain a candidate product. If this candidate product is greater than 9, it is reset to 0 to ensure the final product is a whole number.

Here is a slightly modified version of the code to make the explanation clearer:
```python
def multiply(a, b):
    # Extract the unit digit of the first number
    dig1 = a % 10
    
    # Extract the unit digit of the second number
    dig2 = b % 10
    
    # Multiply the unit digits
    product = dig1 * dig2
    
    # If the product is greater than 9, it will be a decimal number, so we set it to 0
    # to ensure the result is a whole number
    if product > 9:
        product = 0
    
    # Return the final product of unit digits
    return product
```

This code assumes that the input is valid, as stated in the problem statement. It does not check for validity, nor does it handle any potential exceptions that might occur with invalid input. Instead, it jumps straight to calculating the product of the unit digits and returns the whole number result.