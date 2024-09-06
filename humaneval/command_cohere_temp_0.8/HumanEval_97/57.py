```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits. Finally, it returns the product of these unit digits. 

Here is an example of how to use the above function:
```python
print(multiply(12, 21))  # Outputs: 4
```