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

The code assumes that the input is always valid, as stated in the problem statement. If invalid input is possible, additional input validation and error handling would be necessary. 

The unit digit multiplication algorithm is a straightforward approach that efficiently solves the problem, given that the unit digits are multiplied to obtain the product, regardless of the number's size. This is a foundational mathematical strategy for multiplying numbers. 

This solution is optimized for efficiency and is structured concisely to solve the defined problem. It can efficiently handle large and small numbers alike, making it adaptable to various use cases.