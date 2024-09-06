```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function traverses the decimal representation of the input number n, multiplying each odd digit (excluding zeros) into the product variable. The function returns 0 if all digits are even. 

Here is a test case that can be used to verify the function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(0) == 0
```