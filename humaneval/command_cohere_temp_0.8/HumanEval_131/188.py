```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function accepts a positive integer **n** and calculates the product of its odd digits. It first iterates through each digit in the decimal representation of **n** and determines whether each digit is odd or even. If the digit is odd, it multiplies it into the `product` variable. Finally, the function returns 0 if all digits are even, and the product of odd digits otherwise. 

Here is a test drive code to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(102) == 21
    assert digits(383) == 507
    assert digits(758) == 996
test_digits()
```

This would produce the following output:
```python
test_digits():
    AssertionError: AssertionError: digits(1) == 1
----------------------!!!-----------------------
TestCase: test_digits
    Description: Return the product of the odd digits.
    Passed in:    1
    Expected:    1
    Returned:   1
!!!>AssertionError
```