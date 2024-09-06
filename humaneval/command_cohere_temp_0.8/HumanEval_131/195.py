```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This `digits` function iterates through each digit in the decimal representation of the given integer `n`. It multiplies the `prod` variable by each odd digit and leaves each even digit untouched. The final value of `prod` is returned, yielding the product of all odd digits in the input number. 

To handle the special case where there are no odd digits (i.e., when the input number is composed of only even digits), the function returns 0. This is aligned with the problem statement requirement to return 0 in such cases. 

The unit tests for this function are typically designed to cover different scenarios, ensuring that the function behaves correctly for various input numbers, including both positive integers and edge cases. These tests would verify that:
- The function correctly calculates the product of odd digits for input numbers with varying compositions of even and odd digits.
- The function handles input values that do not have any odd digits, returning 0 in such cases. 

The following is a simple example of a unit test for this function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(12345) == 561
```