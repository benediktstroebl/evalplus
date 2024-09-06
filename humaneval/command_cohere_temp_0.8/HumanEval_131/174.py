```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer to a string to iterate through its digits. For each odd digit (ones with a digit % 2 == 1), it multiplies this digit with the `product` variable, which starts at 1 and updates by multiplying with each odd digit encountered. Finally, it returns the resulting product of odd digits.

Here is a self-contained Python script that can be executed to test the above function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 3
    assert digits(8726) == 1731472
    assert digits(525) == 15625

test_digits()
```

The function can be invoked with a variety of inputs to validate its behavior and ensure that it adheres to the given problem statement.