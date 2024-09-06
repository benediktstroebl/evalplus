```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called truncate_number, which takes a single argument number. This function returns the decimal part of the input number by subtracting the largest integer less than or equal to the number from it. This operation effectively captures the fractional part of the number and returns it as the result. 
```python
# Test suite
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.8) == 0.2
```
The test suite included consists of three test cases that cover different scenarios. Each test case asserts that the result of truncate_number matches the expected value, ensuring that the function behaves as intended for a variety of input numbers. 
This approach allows developers to verify the correctness of the code and ensure that it meets the requirement of returning the decimal part of the input number.