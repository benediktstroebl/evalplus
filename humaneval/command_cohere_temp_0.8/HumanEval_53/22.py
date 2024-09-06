```python
def add(x: int, y: int):
    return x + y
```
```python
>> add(2, 3)
5
>> add(5, 7)
12
```
```python
# Test suite with two test cases that check the correctness of the add function
def test_add_correctness():
    assert add(2, 3) == 5, "Expected 5, but got {actual}".format(actual=add(2, 3)) 
    assert add(5, 7) == 12, "Expected 12, but got {actual}".format(actual=add(5, 7)) 
```

This script defines a function called add, which takes two integers as input and returns their sum. The function is tested by the test suite through two test cases, each of which calls the function with different input values and checks that the output is as expected. 

The assert statements within the test suite will throw an AssertionError with a helpful message if the assert condition is not met, which would happen if the add function did not return the expected output. 

If the tests do not generate any errors, you will see an indication that the test suite was successful, and you can proceed confident that the add function works as expected.