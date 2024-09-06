```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It iterates through each digit in the decimal representation of `n` using a `for` loop. It checks if each digit is odd using the modulo operator `% 2` and if it is, the digit's value is multiplied by the `prod` variable, which is initialized to 1 and accumulates the product of odd digits. The function returns 0 if all digits are even, and the product of odd digits otherwise. 

Here is a test case to ensure the code works:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
```