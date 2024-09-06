```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer `n` to a string to iterate through its digits. For each digit, it checks if the digit is odd using the modulo operator. If the digit is odd, it multiplies the `prod` variable by that digit. Finally, it returns the `prod` variable as the product of the odd digits, and it returns 0 if all digits are even.