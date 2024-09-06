```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of each number. The unit digit is the digit at the far right of the number, excluding any decimal point. The function achieves this by using the built-in function `str` to convert the integers to strings, shift the unit digit to the left through slicing (`str(a)[-1]` and `str(b)[-1]`), and then converts it back to an integer for the multiplication. 

Let's test it with the examples provided:
```python
test_multiplication = [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20)
]
for n, m, result in test_multiplication:
    assert multiply(n, m) == result
```
This block of code tests the `multiply` function with a list of test cases including integer inputs `n` and `m` and the expected `result`. The `assert` statement checks if the `multiply` function returns the expected result for each test case. 

The test suite will pass if the `multiply` function returns the correct values for the test cases.  This way, the code can be deemed to have fulfilled the requirements of the problem prompt.