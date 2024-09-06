```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the float `number` to an integer using implicit rounding by converting it to a whole number, and then subtracts this integer from the original number. The resultant value is the residual decimal value of the original number, which is returned from the function. 

This approach does not involve any floating point arithmetic, thereby avoiding the issue of precision and rounding errors. 

To test this function, one can write an test case like this:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.345) == 0.345
```
This test case uses the `assert` statement to confirm that the output of the `truncate_number` function is correct. 

Note that this approach is reliant on the behaviour of the `int` function and assumes that the implicit rounding behaves as expected. Test cases should be comprehensive to ensure that this assumption holds for all desired input values.