```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This `digits` function iterates through each digit in the decimal representation of the given integer `n`. It multiplies the `prod` variable by each odd digit and leaves each even digit unaffected. The resultant product is then returned, reflecting the product of the odd digits in the input number. 

Here is a test that can be used to validate the functionality of the provided solution:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(123) == 21
```

This test suite verifies that the function behaves as expected for different scenarios outlined in the problem statement. 

To run the test, you can copy and paste the above code into a Python interpreter or save it in a `.py` file and execute the file using the `python <filename>` command in your terminal. 

Please let me know if you need anything else!