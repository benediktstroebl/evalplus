```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number to a string to easily iterate over its digits. For each digit, if it is odd (i.e., its remainder when divided by 2 is 1), it multiplies this digit with the evolving product `prod`. Finally, it returns this product, resulting in the desired output for the given problem. 

This solution should correctly solve the problem for any valid input `n`, as it considers each digit individually and appropriately handles the product computation.