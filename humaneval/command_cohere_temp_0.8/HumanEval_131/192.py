```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This Python script defines a function named `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of the input number `n`. For each digit, it checks if the digit is odd using the modulo operator (`int(digit) % 2 == 1`). If the digit is odd, it multiplies the `prod` by the value of that odd digit. Finally, the function returns the value of `prod`, which gives the product of all odd digits in the input number.

This solution is efficient because it utilizes direct manipulation of the decimal representation of the number without converting the input to a list of digits. It also doesn't create any additional unnecessary variables and optimizes the calculation by avoiding redundant loops.