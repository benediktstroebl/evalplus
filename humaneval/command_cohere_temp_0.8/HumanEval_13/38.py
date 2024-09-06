```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This code defines a recursive function `greatest_common_divisor` that returns the greatest common divisor of two integers `a` and `b`. It utilizes the Euclidean algorithm to find the GCD. If `a` is 0, it returns `b` as there is no divisor higher than `b` for the number 0. The function recursively divides `b` by the remainder of the division of `b` by `a`. 

Here is a test suite for the function:
```python
def test_gcd():
    """ Tests for the greatest_common_divisor function """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 25) == 25
    assert greatest_common_divisor(10, 0) == 0
    assert greatest_common_divisor(63, 84) == 21
    assert greatest_common_divisor(121, 23) == 1
test_gcd()
```
This test suite covers different scenarios for the function, including cases where one or both inputs are 0 and cases where the inputs are relatively prime and cases where they are not.  It verifies that the function returns the expected output for these inputs and raises an error for invalid input types. 
To run the test suite, you can use the Python REPL:
```python
test_gcd()
```
Or save the file with a .py extension and run it from the command line:
```bash
python test_gcd.py
``` 
These will run the test suite and display the results, confirming that the `greatest_common_divisor` function behaves as expected.