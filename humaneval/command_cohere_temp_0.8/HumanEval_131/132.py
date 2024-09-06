```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This `digits` function iterates through each digit in the decimal representation of `n`, if a digit is odd, it multiplies it into the `prod` variable, which is initialized to 1. Ultimately, the function returns the value of `prod` which will be zero if all digits are even, and the product of all odd digits otherwise. 

Here is a test case that can be used to verify the function:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
```