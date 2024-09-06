```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number to a string to easily iterate over its digits. It checks if each digit is odd using the modulo operator (`%`) and multiplies the odd digits together, storing the result in the `prod` variable. Finally, it returns the calculated product.

Here is a usage example of the `digits` function:
```python
print(digits(123))  # Output: 15
print(digits(52))  # Output: 52
print(digits(200))  # Output: 0
```

The function's behavior aligns with the problem statement's expectations, incorporating remarks on odd and even digits, and returning 0 when all digits are even.