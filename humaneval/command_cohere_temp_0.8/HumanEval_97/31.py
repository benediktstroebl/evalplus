```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operation `% 10`, and then multiplies these unit digits. To handle the cases where the product of the unit digits exceeds 9, the function employs modular arithmetic again to ensure the result fits within the range of 0 to 9. This approach guarantees the correct computation of the product's unit digit. 

This solution encompasses the entire problem statement, providing a self-contained Python function that can be readily deployed to solve the specific task outlined in the prompt.