```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits to obtain a candidate result. If this candidate result is larger than 9, it means there are carries, so the function resets the result to 0 and returns 0 as the final answer. 

This code assumes that the inputs are valid integers, as stated in the problem statement. Feel free to ask if you would like any further explanations or code refinements!