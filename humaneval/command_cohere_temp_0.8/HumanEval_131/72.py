```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It first initializes a variable `prod` to 1, which will store the final result. Then, it iterates through each digit in the string representation of `n`, checking if each digit is odd using the modulo operator (`%`). If the digit is odd, it multiplies the current value of `prod` by that digit. Finally, it returns the calculated product of odd digits, or 0 if all digits are even.

Here is a test suite to ensure that the function behaves as expected:
```python
def test_digits():
    # Test cases
    tests = [
        (1, 1),
        (4, 0),
        (235, 15),
        (2 344 2326, 2176),
        (1234567890, 277480042),
    ]

    for n, expected in tests:
        result = digits(n)
        assert result == expected, f"For input {n}, expected {expected}, got {result}"

test_digits()
```

This test suite contains a list of test cases with corresponding expected values. It iterates through each test case, calls the `digits` function with the input, and compares the result with the expected value using the `assert` statement. If the assertion passes for all test cases, the test suite will return a passing status.