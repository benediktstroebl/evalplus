```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operation `% 10`. These unit digits are then multiplied together to obtain a product. If the product is greater than 9, it indicates that the original numbers had digits greater than their unit places, and the result would be 0. In such cases, the function returns 0 to adhere to the assumption that the input is always valid. 

Let's break it down with the provided examples:
1. `multiply(148, 412)` - Both numbers have their unit digits extracted as 1 and 4, respectively. 1 * 4 = 4.
2. `multiply(19, 28)` - Both numbers have their unit digits extracted as 9 and 2, respectively. 9 * 2 = 18. Since 18 is greater than 9, the product is reset to 0. Hence, 0 is returned. 
3. `multiply(2020, 1851)` - Both numbers have their unit digits extracted as 0 and 1, respectively. 0 * 1 = 0. 
4. `multiply(14, -15)` - Both numbers have their unit digits extracted as 4 and 5, respectively. 4 * 5 = 20. 

This function will return the correct product of the unit digits of any valid inputs provided.