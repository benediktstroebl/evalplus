```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This script defines a function `digits` that calculates the product of all odd digits in the positive integer `n`, and returns 0 if all digits are even. It achieves this by iterating through each digit in the decimal representation of the number `n` and multiplying each odd digit found by the running product. The function utilizes an internal variable `prod` to keep track of the accumulating product of odd digits, initially set to 1. Ultimately, the function returns the computed product of odd digits.