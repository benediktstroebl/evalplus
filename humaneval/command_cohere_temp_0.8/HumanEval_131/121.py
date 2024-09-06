```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This script defines a function, `digits`, which accepts a positive integer as an argument and returns the product of its odd digits. The function iterates through each digit in the decimal representation of the given number, checking if the digit is odd. If it is, the function multiplies the current value of the `product` by that digit. Finally, the function returns the computed product or 0 if all digits are even.

Here is an example usage of the script:
```python
result = digits(235)
print(result)  # output: 15
```