```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operation (`modulo 10`, which retains the last digit and discards the rest). These unit digits are then multiplied together to obtain the `product`. If the `product` is greater than 9, it adjusts it to 0. Eventually, the function returns the `product` of the unit digits. 

This solution adheres to the problem's assumption that the input is valid, and it appropriately addresses the examples provided in the problem statement. 

You can use this code to solve the problem and achieve the desired outcome. Let me know if you have any further questions or if you'd like to discuss more details.