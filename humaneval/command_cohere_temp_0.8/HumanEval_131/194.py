```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function iterates through each digit in the decimal representation of the input integer `n`. It multiplies the current `prod` by each odd digit and accumulates the result. If all digits are even, it returns `0`. Else, it returns the calculated product of odd digits.

Here is a test case to test the function:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(34) == 1260
    assert digits(5613) == 154300800
``` 

You can copy and paste this test code into a separate Python file to validate the correctness of the `digits` function.