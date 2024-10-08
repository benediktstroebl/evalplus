```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number `n` to a string to iterate through its digits. For each digit, it checks if the digit is odd or even, multiplying the odd digits to calculate the product. In case all digits are even, it returns 0. The algorithm gracefully handles different input scenarios, ensuring accurate result computation.