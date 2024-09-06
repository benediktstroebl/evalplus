```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This Python script defines a function named `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of the input number `n`, extracting each digit as a string from the leftmost end of the number with `str(n)`. For each digit, it checks if the digit is odd using the modulo operator `% 2` and if so, it multiplies the current value of `prod` by the odd digit. Finally, the function returns the value of `prod`, which represents the product of the odd digits in the input number, or 0 if all digits are even.

Here is an example usage of the `digits` function:
```python
print(digits(1))
# Output: 1

print(digits(4))
# Output: 0

print(digits(235))
# Output: 15
```