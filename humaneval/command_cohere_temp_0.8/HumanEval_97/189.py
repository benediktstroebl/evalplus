```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operation `% 10`, and then multiplies these unit digits. To handle the case where the product of the unit digits exceeds 9, the function employs modular arithmetic again to ensure the result fits within a single digit, ultimately returning the product of the unit digits. 

This solution adheres to the problem statement and assumes that the input is valid, as it should. Let's go through the steps of the solution:
1. Two integers `a` and `b` are passed to the `multiply` function. 
2. The unit digit extraction is done via `dig1 = a % 10` and `dig2 = b % 10`, where `%` is the modulo operator, and `10` is used as the divisor to extract the last digit. 
3. The product of the unit digits is calculated as `product = (dig1 * dig2) % 10`. The `*` operator performs the multiplication, and `% 10` ensures the result is modular with respect to 10, keeping the result within a single-digit. 
4. Finally, the function returns the product of the unit digits (`product`). 

This solution effectively computes the product of the unit digits of two integers while ensuring the result remains within a single-digit representation.