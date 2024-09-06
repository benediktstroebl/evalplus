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

This code encapsulates the logic required to solve the problem and can be imported and invoked as a module to solve the given problem.