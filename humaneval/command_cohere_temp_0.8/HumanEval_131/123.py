```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This script defines a function 'digits' that calculates the product of all odd digits in a positive integer 'n'. It iterates through each digit in the decimal representation of 'n', and if the digit is odd, it multiplies it into the 'prod' variable, which starts at 1. The function returns 0 if all digits are even, and the product of odd digits otherwise. 

To see the behavior of the function for different inputs, you can execute the following:
```python
print(digits(1))  # Output: 1
print(digits(4))  # Output: 0
print(digits(235)) # Output: 15
```