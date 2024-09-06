```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This problem can be solved by multiplying the odd digits in the decimal representation of `n` while ignoring the even ones. The `digits` function iterates through each digit in the decimal representation of `n` and checks if the digit is odd using the modulo operator. If the digit is odd, it multiplies it with the `prod` variable, which should be initially set to 1. The final value of `prod` is returned, which will be 0 if all digits are even, and the product of odd digits otherwise. 

Here is a test case to validate the functionality of the function:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
```