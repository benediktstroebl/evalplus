```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This Python script defines a function called `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the string representation of the input number, checking if each digit is odd using the modulo operator %. If the digit is odd, it multiplies the `prod` by the value of that digit. Finally, the function returns the value of `prod`, which gives the product of the odd digits of the input number.

This approach efficiently solves the problem by directly manipulating the individual digits of the input number and avoiding any unnecessary conversions or extra iterations.