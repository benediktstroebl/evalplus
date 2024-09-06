Here is a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

#Test case 1
def test_strlen():
    assert strlen('') == 0 

#Test case 2
def test_strlen2():
    assert strlen('abc') == 3 

#Test case 3
test_strlen3 = lambda: assert strlen('') != 0

#Main code
test_strlen()
test_strlen2()
test_strlen3()
```
This code defines a function `strlen` that calculates the length of a given string. The function is self-contained and has no external dependencies. The test cases ensure the required behavior of the `strlen` function. The test cases are defined as normal functions with assertions that check the expected behavior of the `strlen` function. The main code then invokes the test cases to run and verify the correctness of the function.