```python
def add(x: int, y: int):
    return x + y
```
```python
# Test add function
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12

def test_add_negative():
    assert add(-2, -3) == -5
    assert add(-5, -7) == -12
```
This code defines a function called add which takes two integers as arguments and returns their sum. The function is tested twice; in the first test, it succeeds by adding 2 and 3 and comparing the result to 5, and the second test succeeds by adding 5 and 7 and comparing the result to 12. The second test uses pytest to assert the expected behavior of the function when dealing with negative numbers.  This code demonstrates how to define and test a simple function using Python's built-in assert statement. 
The tests are defined in a separate block, following the conventions of unit testing frameworks like PyTest.  This structure enhances the readability of the code and clearly separates the functionality from the testing logic.  By using pytest, the code can leverage a wide range of powerful testing capabilities that streamline the process of constructing comprehensive and robust tests.