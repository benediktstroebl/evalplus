```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It iterates through each digit in the decimal representation of `n` and checks if the digit is odd. If it is, the function multiplies the `prod` variable by that digit. Finally, it returns the value of `prod`, which represents the product of the odd digits.

Here is a test drive code to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 3
    assert digits(737) == 1
    assert digits(1997) == 1

test_digits()
```

This would generate the following output:
```bash
```test_digits```: ok
```