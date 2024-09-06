```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits. The result is again reduced to the unit digit using the modulo operator to handle the possible overflow of the decimal digits and to retain only the unit digit of the product. This approach ensures that the function will correctly return the unit digit of the product, even in cases where the original numbers have large digits that would typically cause overflow without the modulo operations. 

This solution goes inline with the 'Simplest Solution' paradigm as it focuses on keeping the logic straightforward without introducing extraneous variables or additional steps.