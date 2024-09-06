```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This Python script defines a function named `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable called `product` with a value of 1. Then, it iterates through each digit in the string representation of the input number, checking if each digit is odd using the modulo operator (`%`). If a digit is odd, it multiplies it with the `product`, updating it accordingly. Finally, the function returns the value of `product`, which represents the product of the odd digits in the input number.

Here is a test drive code to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 3
    assert digits(8765) == 585
    assert digits(100000) == 1000000
    assert digits(1234567) == 347
    assert digits(9988887777) == 6628203969
test_digits()
```

This test drive code will validate the correctness of the `digits` function with different inputs.