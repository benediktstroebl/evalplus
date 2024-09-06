Here is a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Testing the function
def testStrlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('123') == 3
    assert strlen('') == 0  # Should return 0
    assert strlen('abcde') > 3  # Should return 4

testStrlen()
```
This code defines a function `strlen` that calculates the length of a given string, and a test function `testStrlen` that verifies the correctness of the function with a set of test strings.

You can use the `testStrlen()` function to run the tests. The function tests the validated against a set of test cases and will provide a pass or fail status, which demonstrates the correct operation of the `strlen` function.