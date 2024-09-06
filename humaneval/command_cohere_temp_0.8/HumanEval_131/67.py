```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function accepts a positive integer **n** and calculates the product of its odd digits. It first iterates through each digit in the decimal representation of **n** and determines whether each digit is odd or even. If the digit is odd, it multiplies it into the **product** variable. Finally, the function returns 0 if all digits are even, and the product of odd digits otherwise. 

Here is a test case to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(102) == 21
```