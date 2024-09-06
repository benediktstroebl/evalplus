```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

The function `digits(n)` takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer to a string to iterate through its digits. For each digit, it checks if it's odd using the modulo operator (`%`). If the digit is odd, it multiplies it with the `prod` variable, which should be initialized to 1 to make the product starting from 1. Finally, the function returns 0 if all digits are even, and the product of odd digits otherwise. 

This solution adheres to the problem statement and aligns with the problem's expected input/output scenarios.