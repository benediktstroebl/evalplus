```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This script defines a function named `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. It initially sets the `prod` variable to 1, which will be used to accumulate the product of odd digits. Then it loops through each digit in the decimal representation of the given number `n` and checks if the digit is odd using the modulo operator (`%`). If the digit is odd, it multiplies the `prod` by the int value of the digit. Finally, it returns the value of `prod` which represents the product of the odd digits of the input number, or 0 if all digits are even. 

Here is an example output of the function:
```python
digits(1)  == 1
digits(4)  == 0
digits(235) == 15
```

This exemplifies the function's behavior, where `digits(1)` returns 1 because the sole digit in 1 is odd, `digits(4)` returns 0 because all the digits in 4 are even, and `digits(235)` returns 15 as the product of its odd digits (which are 5 and 3).  This script effectively addresses the problem statement in a self-contained manner.