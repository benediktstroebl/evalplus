```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This Python script defines a function named `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of the input number `n`, extracting each digit as a string from the left of the decimal point. For each digit, it checks if the digit is odd using the modulo operator (`int(digit) % 2 == 1`). If the digit is odd, it multiplies the current value of `prod` by the odd digit. This process continues for all odd digits, effectively calculating their product. Finally, the function returns the value of `prod`, which represents the product of the odd digits in the input number.

This approach ensures that the function handles both positive integers and edge cases correctly as specified in the problem statement.