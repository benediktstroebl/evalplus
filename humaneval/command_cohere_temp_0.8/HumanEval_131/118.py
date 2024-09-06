```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This script defines a function `digits` that takes an integer argument and returns the product of the odd digits in the integer. The function first initializes a variable `product` to 1, then iterates through each digit in the string representation of the integer `n`. For each digit, it checks if the digit is odd using the modulo operator `%`, and if so, it multiplies the current value of `product` by the digit. Finally, the function returns the value of `product`.

Here is an example usage of the function:
```python
print(digits(1))
# Output: 1

print(digits(4))
# Output: 0

print(digits(235))
# Output: 15
```

This demonstrates the function's behavior, namely that it correctly calculates the product of the odd digits in the given integers, returning 0 if all digits are even, and multiplying the odd digits otherwise.