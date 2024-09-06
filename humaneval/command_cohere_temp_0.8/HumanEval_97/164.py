```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers a and b as input, extracts the unit digits of both numbers using the expression `a % 10` and `b % 10` respectively, and then calculates the product of these unit digits. Finally, it returns the result. 

This solution assumes that the inputs are valid, which means that they are integers and their unit digits are numbers from 0 to 9. Therefore, it assumes that the input will handle edge cases like a number ending in .5 or -.5 which would need to round the number to validate the use of `% 10`. It also assumes that the integers are not 0 to handle cases like multiply(0, 12), which would throw a TypeError. 

This solution provides a straightforward way of completing the function as per the provided problem statement.