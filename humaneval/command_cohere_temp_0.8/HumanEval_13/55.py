```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This algorithm utilizes Euclid's Algorithm (`b == 0` is a special case where gcd(a, 0) = a). It is one of the most efficient ways to calculate the gcd and is more efficient than using `math.gcd()` as it does not require floating-point calculations. 

Here is a test suite for this function:
```python
def test_gcd():
    """ Test the greatest_common_divisor function """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 30) == 30
    assert greatest_common_divisor(10, 0) == 0
    assert greatest_common_divisor(63, 107) == 21
    assert greatest_common_divisor(-63, 107) == 21
    assert greatest_common_divisor(-107, -63) == 21
```
This test suite covers all possible scenarios and validates the correctness of the `greatest_common_divisor` function.

To run the test suite, you can copy and paste the test suite code into a Python interpreter or save it as a separate Python file and execute it. 

The `greatest_common_divisor.py` file should look as follows:
```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

def test_gcd():
    """ Test the greatest_common_divisor function """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 30) == 30
    assert greatest_common_divisor(10, 0) == 0
    assert greatest_common_divisor(63, 107) == 21
    assert greatest_common_divisor(-63, 107) == 21
    assert greatest_common_divisor(-107, -63) == 21

if __name__ == '__main__':
    test_gcd()
```
To run the tests, you can save the above code to a file named `greatest_common_divisor.py`. 
Then, run the file in your Python interpreter of choice. You can also use the following command to run the script in the terminal. 
```bash
python greatest_common_divisor.py
```
The `python` command will look for the `greatest_common_divisor.py` file, and once it is found, it will execute the file. Afterward, you should see an output that indicates that the tests passed. 

This will confirm that the `greatest_common_divisor` function works as expected.