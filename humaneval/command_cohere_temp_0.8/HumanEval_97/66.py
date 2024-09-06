```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits to obtain a candidate result. If this candidate result is greater than 9, it means there are carrying digits, so the function resets the result to 0 and returns it. This behavior is consistent with the rule that the unit digit of the product of two numbers is the multiplication of their unit digits, and any carrying digits should result in a unit digit of 0. 

This algorithm efficiently solves the problem using a straightforward approach and avoids any complexity associated with manipulating the whole numbers or unnecessary assumptions about the behavior of the carrying digits.