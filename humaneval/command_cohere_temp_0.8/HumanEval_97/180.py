```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits. If the result of this multiplication is greater than 9, it means there's a two-digit number, so the function applies a second modulo operation to truncate it back to a single digit. Ultimately, it returns the product of the unit digits of a and b. 

The test cases provided in the prompt exercise different scenarios and validate the correctness of the solution. Feel free to add this script to your codebase, and you can modify the tests or the function accordingly to match your needs.