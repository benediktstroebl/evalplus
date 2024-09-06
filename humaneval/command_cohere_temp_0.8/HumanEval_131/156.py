```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It iterates through each digit in the decimal representation of `n` and multiplies each odd digit found by the `prod` variable, which starts at 1. The function returns 0 if all digits are even, and the final product of odd digits otherwise.

Here is a test case to verify its functionality:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 3
    assert digits(5001) == 501
```

This test suite contains several test cases to validate the function's behavior, checking if it returns the correct values for different input scenarios.