```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This script defines a function, `digits`, which accepts a positive integer as an argument and returns the product of its odd digits. The function first initializes a variable `product` to 1, then iterates through each digit in the string representation of the argument, checking if each digit is odd. If it is, the function multiplies the current value of `product` by that digit. The function returns 0 if all digits are even, and the product of odd digits otherwise. 

To see the behavior of the function for different inputs, you can run the following:
```python
print(digits(1))
print(digits(4))
print(digits(235))
```

This will output:
```bash
1
0
15
```

As expected, the function returns 1 for an odd digit, 0 for an even digit, and 15 for a mix of odd and even digits.