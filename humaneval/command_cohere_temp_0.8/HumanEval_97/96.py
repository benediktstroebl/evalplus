```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The code solves the problem by extracting the unit digits of both numbers using the modulo operation (`a % 10` and `b % 10`). These unit digits are then multiplied together to get the product of the unit digits, `dig1 * dig2`. Since the product of two single-digit numbers is less than 10, it is sufficient to consider only the tens digit of the result, i.e., `product`. 

Finally, the function returns the product of the unit digits, considering the scenario where the result is greater than 9 and adjusting it to ensure it's a single-digit number.

This solution efficiently computes the product of the unit digits of two integers, adhering to the problem's assumption of valid input.