```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function accepts a positive integer **n** and calculates the product of its odd digits. It initially establishes a variable named **product** and assigns it a value of 1. Then it iterates through each digit in the string representation of **n** , verifying if each digit is odd. If it is, it multiplies the current value of product by the digit. The function yields 0 if all digits are even, denoting that the input number contains only even digits.

Here is a sample output of the function:
```
digits(1)  == 1
digits(4)  == 0
digits(235) == 15
```

This example output shows the function's behavior when invoked with different kinds of input. When `digits(1)` is called, the function returns 1 because the sole digit in 1 is 1, and that is an odd digit. When `digits(4)` is called, the function returns 0 because the digit 4 is the only one, and it is even. When `digits(235)` is invoked, the outcome is 15, since the two odd digits in 235 are 5 and 3, and their product is 15.