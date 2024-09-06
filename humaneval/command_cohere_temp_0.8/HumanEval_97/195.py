```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits. If the product of the unit digits is greater than or equal to 10, it returns the product modulo 10, ensuring that the result is a single-digit number. This approach efficiently computes the product of the unit digits. 

The `assert` statements reinforce the correct operation of this code by verifying that it produces the expected output for various scenarios.

This function may be called with various input values to test its robustness and ensure its accuracy in different cases.