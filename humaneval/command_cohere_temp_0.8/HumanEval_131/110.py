```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This problem can be solved by multiplying the odd digits in the integer representation of `n`. The self-contained Python script provides a `digits` function that achieves this aim. It first initializes a `prod` variable to 1, which will be used to accumulate the product of odd digits. It then loops through each digit in the string representation of `n`, checking if the digit is odd using the modulo operator. If the digit is odd, it multiplies the `prod` value by that particular digit. Finally, the function returns the value of `prod`, which gives the product of all odd digits in the input number. 

This solution works well for positive integers and handles cases where all digits are even or some/all digits are odd.