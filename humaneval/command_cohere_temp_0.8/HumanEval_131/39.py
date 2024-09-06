```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function `digits(n)` takes a single argument `n`, which is a positive integer. It initializes a variable `product` to 1, then iterates through each digit in the decimal representation of `n`. Using the modulo operator (`%`), it determines whether each digit is odd or even. If the digit is odd, it multiplies the `product` by that digit. Finally, it returns the `product` of the odd digits, or 0 if all digits are even.

Here is a test drive code to test the above function:
```python
def test_digits():
    # Test cases
    tests = [
        (1, 1),
        (4, 0),
        (235, 15),
        (2354, 0),
    ]

    for n, expected in tests:
        actual = digits(n)
        assert actual == expected, f"For input {n}, expected {expected}, but got {actual}"

test_digits()
```

The `test_digits()` function provides a list of test cases with given inputs and expected outputs, systematically validating the `digits()` function against expected behavior. Each test is executed within the `test_digits()` function, and the assertion at the end verifies that actual output matches the expected outcome for each test case.