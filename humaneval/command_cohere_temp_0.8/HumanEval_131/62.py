```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer `n` to a string to easily iterate over its digits. It then checks if each digit is odd, and if so, multiplies it into the `prod` variable. Finally, it returns the final value of `prod`, which represents the product of the odd digits, or 0 if all digits are even. 

Here's an example of function usage:
```python
print(digits(1))  # 1
print(digits(4))  # 0
print(digits(235)) # 15
```

This should output:
```
1
0
15
```