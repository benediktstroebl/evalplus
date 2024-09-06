```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This script defines a function 'digits' that calculates the product of all odd digits in a positive integer 'n' and returns 0 if all digits are even. It achieves this by iterating through each digit in the decimal representation of 'n' and multiplying the odd digits into the 'prod' variable, which tracks the final result.