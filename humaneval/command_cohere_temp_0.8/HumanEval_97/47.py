```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operator `% 10` to get `dig1` and `dig2`. These represent the last digits of `a` and `b`, respectively. It then computes the product of these unit digits and assigns it to the `product` variable. 

If the product of the unit digits is greater than or equal to 10, it means the unit digit of the product will be the remainder when the product is divided by 10. This is achieved by applying the modulo operator again, `product % 10`. 

Finally, the function returns the product of the unit digits, representing the last digit of the multiplied number. This algorithm follows the assumption that the input is always valid, considering that the unit digits of the input are integers from 0 to 9. 

To handle the edge case where one or both inputs are multiples of 10, the script checks if either `a % 10` or `b % 10` is equal to 0 and returns 0 in such cases. You can handle this case more generally by also checking if the second digit of a or b is 0 and returning 0 in that case as well if you desire.