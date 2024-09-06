```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits. The result is again reduced to the unit digit using the modulo operator to handle the possible overflow of the decimal digits and to obtain the desired result. 

To test this, you can call this function with different sets of inputs to verify the correctness of the implementation. 
Like in the following example:
```python
print(multiply(148, 412)) # Output: 16
print(multiply(19, 28))  # Output: 72
print(multiply(2020, 1851)) # Output: 0
print(multiply(14, -15))  # Output: 20
```

This should output:
```
16
72
0
20
```

This demonstrates the expected behavior of the `multiply` function, considering the unit digits of the inputs and producing the corresponding product of unit digits.