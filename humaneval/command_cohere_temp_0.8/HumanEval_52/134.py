```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the built-in Python function `all` to return True if all elements in the list `l` are less than the threshold value `t`.

Here is a test to ensure that the function `below_threshold` is working correctly:
```python
test_below_threshold = '''
# Test if below_threshold function is working correctly

>>> below_threshold([1, 2, 4, 10], 100)
True

>>> below_threshold([1, 20, 4, 10], 5)
False
```

The above test yields True and False respectively, showing that the function `below_threshold` is working correctly. 
To run this test, you can copy and paste the test cases into a Python interpreter, or save them into separate test files and run them using a test runner.