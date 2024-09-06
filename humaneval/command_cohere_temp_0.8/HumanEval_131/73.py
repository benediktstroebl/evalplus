```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This Python script defines a function called `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of the input number `n`, extracted using the `str(n)` conversion. For each digit, it checks if the digit is odd using the modulo operator `% 2`. If the digit is odd, it multiplies the `prod` by the value of that digit `int(digit)`. Finally, the function returns the value of `prod`, which gives the product of the odd digits of the input number.

The mdfile.py test file accompanies this script and contains a test suite with a single test case to ensure the correctness of the `digits` function. The test case checks if the function's output matches the expected result for a specific input, asserting that the function returns the correct product of odd digits for different input scenarios.