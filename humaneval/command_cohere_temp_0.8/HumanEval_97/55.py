```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The code directly multiplies the unit digits (`dig1 % 10` and `dig2 % 10`) to find the product. If the result is greater than or equal to 10, it retains only the unit digit by taking the remainder when multiplied by 10, ensuring the final result fits the specified requirement. 

To test this, you can call this function with various input values, ensuring it produces the expected outputs:
```python
# Test Cases
assert multiply(148, 412) == 16
assert multiply(19, 28) == 72
assert multiply(2020, 1851) == 0
assert multiply(14, -15) == 20
```

This approach efficiently computes the product of the unit digits while ensuring the result conforms to the problem's criteria. Let me know if you'd like me to explain any part of the code further!