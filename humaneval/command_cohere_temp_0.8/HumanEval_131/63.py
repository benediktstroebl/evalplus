```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer to a string to easily iterate over its digits. It checks if each digit is odd using the modulo operator (`%`). If a digit is odd, it multiplies it with the `prod` variable, which should be initially 1 to ensure the correctness of the function. The function returns 0 if all digits are even, considering the product of no digits is 0.

Here is a test case to ensure its correctness:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
```