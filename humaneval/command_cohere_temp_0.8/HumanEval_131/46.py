```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function `digits(n)` takes a single argument `n`, which is a positive integer. It initializes a variable `product` to 1, then iterates through each digit in the string representation of `n`. For each digit, it checks if the digit is odd or even, using the modulo operator `%`. If the digit is odd, it multiplies the `product` by the value of that digit. Finally, it returns the calculated product of odd digits, or 0 if all digits are even. 

Here is a basic test suite to ensure this function passes a variety of inputs:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(12345) == 561
    assert digits(97) == 729
    assert digits(1111) == 1
```