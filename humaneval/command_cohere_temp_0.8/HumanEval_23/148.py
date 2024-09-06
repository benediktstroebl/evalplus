```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script provides a function termed `strlen` taking a string argument and returning its length. The function utilizes the built-in Python `len()` method to calculate the number of bytes in the provided string, implying the count of characters assuming the input contains only ASCII characters. 

Here's an example of how to use the `strlen` function:
```python
def test_strlen():
    """ Unit tests for strlen function """
    assert strlen("") == 0
    assert strlen("abc") == 3
    assert strlen("Hello, World!") == 13

test_strlen()
```
This is a simple unit test that checks the `strlen` function for correctness. 

The `strlen` function is then invoked with three different inputs, namely an empty string, a string of three characters, and a longer greeting message. The function is anticipated to return 0 for the empty string, 3 for the three-character string, and 13 for the greeting message. These assertions pass successfully, confirming the accuracy of the `strlen` function. 

To execute this, you can copy and paste the script into a Python environment of your choice.