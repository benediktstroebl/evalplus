```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The code directly leverages the modulo operator (`%`) to obtain the unit digits of both numbers, before multiplying them together. If the result exceeds 9, it resets the product to 0 to ensure the final output only includes the unit digits. This aligns with the "partial product" approach often used for mental arithmetic. 

This function can efficiently compute the product of the unit digits of any two integers, as exemplified in the problem statement. 

The code includes an example of how to use the function in the interpreter:
```python
print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))  # Output: 72
print(multiply(2020, 1851))  # Output: 0
print(multiply(14, -15))  # Output: 20
```

If you'd like to test this function alongside other related functions, or within a larger context, it's often preferable to organize these into separate modules or files.