```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers a and b, extracts the unit digits of both using the modulo operator (`%`), and then multiplies these unit digits. The result is again reduced to the unit digit using the modulo operator to handle the possible large product, ensuring the final result is within the range of integers. 

To test this, you can run the following tests to ensure the function behaves as expected: 
```python
- assert multiply(148, 412) == 16
- assert multiply(19, 28) == 72
- assert multiply(2020, 1851) == 0
- assert multiply(14, -15) == 20
```

Let me know if you need anything else!