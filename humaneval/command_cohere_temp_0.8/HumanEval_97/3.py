```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits. If the result of this multiplication is greater than 9, it means the unit digit of the final product would be less than 10, so the function applies another modulo operation to keep the result's unit digit accurate. Ultimately, the function returns the unit digit of the product. 

This solution assumes that the input is valid and that the arguments are integers.