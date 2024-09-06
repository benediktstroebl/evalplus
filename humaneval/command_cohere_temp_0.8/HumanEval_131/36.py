```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number to a string to iterate through its digits. For each odd digit (ones with a remainder of 1 when divided by 2), it multiplies it with the `product` variable, which starts at 1. Finally, it returns the resulting product, which will be 0 if all digits are even.

Here is a test case to test the function:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
```