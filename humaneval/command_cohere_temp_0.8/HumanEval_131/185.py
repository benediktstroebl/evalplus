```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer `n` to a string to iterate through its digits. For each digit, if it is odd (i.e., its remainder when divided by 2 is 1), it multiplies this digit's value with the `prod` variable, which starts at 1. Finally, it returns the resulting product, which will be 0 if all digits are even, and the expected value if there are any odd digits.