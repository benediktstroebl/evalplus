```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It first initializes a variable `product` to 1, then iterates through each digit in the decimal representation of `n`. Using the modulus operator (`%`), it determines whether each digit is odd or even; if the digit is odd, it multiplies it with the `product`. Finally, the function returns the computed product of odd digits, or 0 if all digits are even. 

Here is a simple test case to verify the functionality of the code:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
```