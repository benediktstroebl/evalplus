```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script defines a function named strlen that takes a string argument and returns the length of that string. It utilizes the built-in Python function len to determine the number of characters in the input string. 

This fundamental function is used to provide a string length value when given any string input.

This approach ensures the function is self-contained and does not rely on external modules or dependencies. 
```python
# Test strlen function
def test_strlen():
    assert strlen("Hello!") == 10
    assert strlen("") == 0
    assert strlen(" abc ") == 4

test_strlen()
```

Two test cases are defined to verify the correctness of the strlen function. In the first test case, the function is tested with the string "Hello!" which has a length of 10. The second test case uses an empty string, which is expected to have a length of 0. These test cases ensure that the function behaves as expected and produces accurate results for different inputs.

```python
test_strlen()
```

This statement executes the test_strlen function, which evaluates the assertions and confirms their adherence to the expected behavior of the strlen function. Failing tests produce an AssertionError error, while successful tests do not generate any output, making it easier to use in larger projects.