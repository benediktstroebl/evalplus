```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This problem can be solved by multiplying the odd digits in the integer representation of `n`. The self-contained function `digits()` takes an integer `n` as input and outputs the product of the odd digits, or 0 if all digits are even. 

To do so, it first initializes a variable `prod` to 1, which will be used to accumulate the product of the odd digits. It then iterates through each digit in the string representation of `n` using a `for` loop and examines the parity of each digit using the modulo operator `% 2 == 1`. 

If the digit is odd, it multiplies the current value of `prod` by the odd digit. This way, it computes the product of all odd digits in the number, and returns this value at the end of the function. 

This solution is efficient because it uses only a single pass through the integer's digits and does not require any additional storage for collecting digits.