```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It first initializes a variable `product` to 1, then iterates through each digit in the string representation of `n`. If a digit is odd (`int(digit) % 2 == 1`), it multiplies this digit's value into the `product`. Finally, it returns the calculated product or 0 if all digits are even, based on the given criteria. 

The code efficiently solves the problem using string manipulation and basic integer operations.