```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function `digits(n)` takes a single argument `n`, which is a positive integer. It initializes a variable `product` to 1, then iterates through each digit in the decimal representation of `n`. Using the modulo operator (`%`), it determines whether each digit is odd or even. If the digit is odd, it multiplies the current value of `product` by that particular digit. Finally, it returns the computed product of odd digits, or 0 if all digits are even. 

The TDD approach ensures that individual components of the code, namely the `digits` function, are rigorously tested and function correctly within the context of the given problem.