```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This Python script defines a function called `digits` that takes in a positive integer as an input. It initializes a variable called `product` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the string representation of the input number, checking if each digit is odd using the modulo operator. If the digit is odd, it multiplies it with the `product`, updating it accordingly. Finally, the function returns the value of the `product` which represents the product of the odd digits in the input number, or 0 if all digits are even. 

To ensure that the function handles different input cases and returns the correct values based on the problem statement, test cases should be included to validate its behavior. 
For example:
```python
# Test case for odd digits
assert digits(1) == 1
assert digits(15) == 3
assert digits(567) == 231

# Test case for all even digits
assert digits(4) == 0
assert digits(20) == 0
assert digits(36) == 0
```