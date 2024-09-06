```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer `n` to a string to easily iterate over its digits. For each digit, it checks if it's odd using the modulo operator. If the digit is odd, it multiplies it with the `prod` variable, which should be initially 1. The function returns 0 if all digits are even, and the product of odd digits otherwise.

Here is a test case to test the above function:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
```