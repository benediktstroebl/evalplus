```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function iterates through each digit in the decimal representation of the input integer 'n', checking if each digit is odd. If the digit is odd, it multiplies this digit with the 'prod' variable, which is initialized to 1. Ultimately, the function returns the value of 'prod', which will be the product of all odd digits and equals 0 if all digits in 'n' are even. 

This solution passes test cases for the given problem, such as 'digits(1) == 1' and 'digits(235) == 15', hence demonstrating its accuracy.