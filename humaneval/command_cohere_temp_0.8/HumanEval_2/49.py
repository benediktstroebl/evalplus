```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the given floating point number and the closest integer to it. The residual value is the desired decimal part, which is always smaller than 1. Given the nature of floating point numbers in Python, this method implicitly depends on the IEEE 754 floating point standard and behaves similarly to `round(x) - x` for non-integer inputs. 

To test this function, you can create a test case that verifies the behavior for a wide range of input values, including non-positive numbers. Here is an example:
```python
def test_truncate_number():
    # Positive integers
    assert truncate_number(1.5) == 0.5
    assert truncate_number(2.0) == 0.0

    # Positive non-integers
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.72) == 0.72

    # Zero
    assert truncate_number(0.1) == 0.0

    # Negative integers
    assert truncate_number(-1.5) == -0.5
    assert truncate_number(-2.0) == -0.0

    # Negative non-integers
    assert truncate_number(-3.5) == -0.5
    assert truncate_number(-7.72) == -0.72

    # Non-positive numbers
    assert truncate_number(-10.0) == -1.0
    assert truncate_number(0.0) == 0.0
    assert truncate_number(-0.1) == -0.1
``` 

This way, you can ensure the function's correctness for all possible inputs.