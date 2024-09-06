```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operation (`modulo 10`, which retains the last digit and discards the rest). These unit digits are then multiplied together to obtain a product. If the result is greater than 9, it undergoes a further modulo operation (%' 10) to ensure the final result is within the range of 0 to 9, representing the unit digit of the product. 

The unit digit is returned as the result of the function. 

This algorithm efficiently computes the product of the unit digits of two integers in O(log(min(a, b))) time, thanks to the reduced precision and the smart handling of the result's unit digit.