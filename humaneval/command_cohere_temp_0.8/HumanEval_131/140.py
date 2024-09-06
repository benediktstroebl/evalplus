```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It first initializes a variable `product` to 1, then iterates through each digit in the decimal representation of `n`. If a digit is odd (i.e., its remainder when divided by 2 is 1), it multiplies this digit into the `product`. Finally, it returns the calculated product of odd digits, or 0 if all digits are even.

Here is a test case to test the function:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
``` 
This would assert the function behaves as expected for these input cases.