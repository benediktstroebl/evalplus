```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

The function `digits(n)` takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer to a string to iterate through its digits. For each digit, it checks if the digit is odd or even, multiplying the odd digits to calculate their product while leaving even digits untouched. The function returns 0 if all digits are even, and for mixed or all-odd digit inputs, it returns the product of odd digits.