```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operation `% 10` to get the last digit regardless of the number's magnitude. It then multiplies these unit digits and applies the modulo operation again to ensure the result is also a unit digit. This way, the function computes the product of the unit digits of the input integers, as per the problem statement. 

This solution focuses on implementing the core logic of the problem in a concise and efficient manner. If you'd like, we can expand this script to include a comprehensive test suite with various input scenarios to fully validate the correctness of the solution.