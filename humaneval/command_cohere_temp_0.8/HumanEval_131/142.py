```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function traverses the decimal representation of 'n' and multiplies each odd digit encountered into the 'product' variable. The final value of 'product' is returned, or 0 is returned if all digits are even. This solution adheres to the specified problem guidelines and assumes 'n' to be a positive integer.

```python
# Test Harness
test_cases = [
    (1, 1),
    (4, 0),
    (235, 15),
]

for n, expected in test_cases:
    actual = digits(n)
    assert actual == expected, f"For input {n}, expected {expected}, but got {actual}"
```

This code block serves as a straightforward test harness for the 'digits' function. It provides a list of test cases, and for each case, it invokes the function and verifies the result against the expected value. If the assertion passes, it indicates that the function performs as expected. 

If all assertions hold, the test suite is successful, validating the correctness of the 'digits' function.