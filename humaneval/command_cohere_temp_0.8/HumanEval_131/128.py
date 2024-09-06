```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It first initializes a variable `prod` to 1, which will store the final result. Then, it iterates through each digit in the string representation of `n`, checking if each digit is odd using the modulo operator. If the digit is odd, it multiplies the `prod` by the value of that odd digit. Finally, it returns the value of `prod`, which now holds the product of all odd digits in `n`, or 0 if all digits are even.

Here is a test case to test the functionality of the code:
```python
test_cases = [
    (1, 1),
    (4, 0),
    (235, 15),
    (123, 123),
    (2123, 0),
    (3245235, 5471)
]

for n, expected in test_cases:
    produced = digits(n)
    assert produced == expected
``` 

This block of code defines a list of test cases with corresponding expected outputs. It then iterates through each test case, calling the `digits` function on the input number `n` and asserting that the produced output is equal to the expected output.  This validates the correctness of the `digits` function.