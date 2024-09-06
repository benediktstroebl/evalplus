```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This script defines a function `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. It initially sets the `prod` variable to 1, which is used to accumulate the product of odd digits. Then it loops through each digit in the decimal representation of the number `n` and determines whether the digit is odd. If it is, it multiplies the `prod` by the digit. It returns 0 if all digits are even, indicating that there are no odd digits in the positive integer `n`. Ultimately, this script encapsulates the problem's requirement to compute the product of the odd digits in a given positive integer `n` within a single function.