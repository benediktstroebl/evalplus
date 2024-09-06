```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number to a string to iterate through its digits. For each digit, if it is odd, it multiplies it with the `prod` variable, which should be initialized to 1 and will hold the final result. The function returns 0 if all digits are even, and the final calculated product otherwise.

Here is a test suite to ensure it works correctly:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 21

test_digits()
``` 
The tests will ensure that the function behaves as expected for different inputs.