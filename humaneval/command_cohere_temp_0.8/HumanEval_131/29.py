```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This problem can be solved by multiplying the odd digits in the integer representation of `n`. The self-contained Python script provides a `digits` function that achieves this aim. It first initializes a `prod` variable to 1, which will be used to accumulate the product of odd digits. It then loops through each digit in the string representation of `n` using a `for` loop and checks if each digit is odd using the modulo operator `% 2`. If the digit is odd, it multiplies the current value of `prod` by the odd digit. Finally, the function returns `prod`, which now holds the product of the odd digits in `n`. 

Note that if all digits in `n` are even, the `prod` variable remains unchanged, which is equal to 1 in the initial state, and the function returns 0 in accordance with the requirement mentioned in the problem description.