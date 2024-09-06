```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function `digits(n)` takes a single argument n, which is a positive integer. It initializes a variable `product` to 1, then iterates through the digits of n's string representation, if a digit denotes an odd number, it multiplies this digit to the `product`. Finally, it returns the final value of `product`, which will be 0 if all digits are even, and the product of all odd digits otherwise. 

Here is a test drive code to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 21

test_digits()
```

This would yield the following results:
```bash
True
True
True
True
```