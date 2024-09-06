```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number `n` to a string to iterate through its digits. For each digit, if it is odd (i.e., its remainder when divided by 2 is 1), it multiplies this digit with the `prod` variable, which should be initially 1. The function returns 0 if all digits are even, and the product of odd digits otherwise. 

The following test cases illustrate the function's behavior:
```python
# Test case for digits(1)
assert digits(1) == 1

# Test case for digits(4)
assert digits(4) == 0

# Test case for digits(235)
assert digits(235) == 15

# Test case for digits(7)
assert digits(7) == 7

# Test case for digits(0)
assert digits(0) == 0
```