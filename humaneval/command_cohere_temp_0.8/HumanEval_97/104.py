```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The code directly computes the product of the unit digits and then returns the result, taking care to remap any products greater than 9 back to their unit digit. This straightforward approach elegantly solves the problem.

This function can be invoked as demonstrated in the problem statement - eg. `multiply(148, 412)`. It can also be embedded within a testing environment to ensure its correctness over a large spectrum of inputs. 

Would you like assistance with anything else? Feel free to ask, whether it's related to this problem or something entirely different!