```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The code directly leverages the modulo operator (`%`) to determine the unit digits of both numbers, before multiplying them and taking the result modulo 10 to ensure it lies within the range of 0 to 9. This approach efficiently computes the product of the unit digits, as required by the problem statement.

Here's the explained solution:
- The function `multiply(a, b)` takes two integers `a` and `b` as inputs.
- To obtain the unit digits, it uses the modulo operator (`%`) to calculate `dig1 = a % 10` and `dig2 = b % 10`, which effectively extracts the last digit from each number.
- Next, the product is calculated by multiplying these unit digits: `product = dig1 * dig2`.
- If the result is greater than or equal to 10, it means the unit digit becomes multiples of 10, so `product` is again modulated by 10 to get the required last digit, i.e., `product = product % 10`.
- Finally, the function returns the product of the unit digits.

This method efficiently solves the problem by directly manipulating the unit digits, providing a straightforward and computationally efficient approach.