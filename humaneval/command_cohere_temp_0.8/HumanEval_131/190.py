```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This Python script defines a function named `digits` that takes in a positive integer as an input. It initializes a variable `product` to 1, which will be used to accumulate the product of odd digits in the input number. The script then iterates through each digit in the string representation of the input number using a `for` loop. For each digit, it checks if the digit is odd using the modulo operator (`int(digit) % 2 == 1`). If the digit is odd, it multiplies the `product` by the value of that odd digit. Finally, the script returns the value of `product`, which represents the product of the odd digits in the input number.

This code efficiently solves the problem by directly manipulating the integer and its digits using Python, resulting in a concise and effective solution.