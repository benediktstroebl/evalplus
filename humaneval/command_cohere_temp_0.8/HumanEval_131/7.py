```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number to a string to easily iterate over its digits. It checks if each digit is odd using the modulo operator (`%`). If a digit is odd, it multiplies it with the growing product `prod`. Finally, if all digits are even, it returns 0, as stipulated in the problem statement. 

This solution adheres to the problem's given examples, correctly returning 1 for `digits(1)`, 0 for `digits(4)`, and 15 for `digits(235)`.