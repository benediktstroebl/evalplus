```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the closest integer (biggest whole number smaller than the given number). This difference is the desired decimal part of the original number. 

Here are some examples of test cases that demonstrate the functionality of the `truncate_number` function:
```python
# Testing the truncate_number function
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.99) == 0.01
    assert truncate_number(11.5) == 0.5
    assert truncate_number(100.0) == 0.0
    assert truncate_number(0.1) == 0.0
    assert truncate_number(10.01) == 0.01
``` 

These test cases use the `assert` statement to verify that the output of the `truncate_number` function is correct for a variety of test cases. 

The `truncate_number` function only works for positive floating point numbers due to the assumption that the 'leftover' part of the number is always smaller than the biggest integer smaller than the number, which is true for floating point numbers that are positive. If the input number is negative or if the decimal part is equal to or greater than 1, the function will no longer accurately represent the original number.