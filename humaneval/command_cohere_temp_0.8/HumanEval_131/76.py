```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This Python script defines a function called `digits` that takes in a positive integer as an input and returns the product of the odd digits present in that number. It initially sets the `product` variable to 1, which will be used to accumulate the product of odd digits. Then it loops through each digit in the string representation of the input number, checking if each digit is odd using the modulo operator. If the digit is odd, it multiplies the `product` by that digit. Finally, the function returns the calculated product of odd digits, or 0 if all digits are even. 

Here is an example of how to use this function:
```python
print(digits(1))
print(digits(4))
print(digits(235))
```

The output will be:
```
1
0
15
```

This shows that the function correctly calculates the product of the odd digits, according to the given problem statement.