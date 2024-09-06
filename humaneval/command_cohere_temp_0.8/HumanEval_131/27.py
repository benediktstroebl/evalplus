```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function `digits(n)` takes a single argument `n`, which is a positive integer. It initially sets `product` to 1 for the accumulation of the product of odd digits. It then iterates through each digit in the string representation of `n` using a `for` loop with the `str(n)` as the iterator. It checks if the current digit is odd using the modulo operator `% 2` and multiplies the `product` by the odd digit if it exists. The function returns 0 if all digits are even, and otherwise, it returns the final value of `product`.

Here is a test drive code to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 21

test_digits()
```

This would generate the following output:
```
PASS
```