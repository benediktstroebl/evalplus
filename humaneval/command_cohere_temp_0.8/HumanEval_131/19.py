```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This `digits` function iterates through each digit in the decimal representation of the given number `n`. It multiplies the odd digits together, contributing to the `prod` variable, and hence produces a result of 0 if all the digits are even.