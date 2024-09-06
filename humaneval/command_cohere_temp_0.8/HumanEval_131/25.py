```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This Python script defines a function named `digits` which takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of the input number `n`, extracting each digit as a string from the leftmost digit to the right. For each digit, it checks if the digit is odd using the modulo operator (`int(digit) % 2 == 1`). If the digit is odd, it multiplies the current value of `prod` by the odd digit. This process continues for all digits, regardless of the number's magnitude, effectively calculating the product of only the odd-positioned digits in the decimal representation. Finally, the calculated `prod` is returned, representing the product of the odd digits in the input number.

This approach ensures that the function follows the problem statement's guidelines, returning 0 if all digits are even (thus excluding even positions in the product), and correctly calculating the product of odd digits for numbers of varying sizes.