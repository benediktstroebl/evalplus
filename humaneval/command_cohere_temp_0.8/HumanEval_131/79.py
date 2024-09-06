```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It iterates through each digit in the decimal representation of `n` using a `for` loop. It initializes a `prod` variable to 1, which will be used to accumulate the product of odd digits. For each digit, it checks if the digit is odd using the modulo operator (`int(digit) % 2`). If the digit is odd, it multiplies the `prod` by the value of that odd digit. Finally, the function returns the value of `prod`, which gives the product of all odd digits in the input number.

Here is a markdown code block depicting the solution above:
```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function effectively calculates the desired product, considering only the odd digits, and returning 0 if all digits are even, as specified in the problem statement.