Here's a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    """
    return len(string)

# Testing the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3

# Example usage
print(strlen('abc'))
``` 
This script includes a function `strlen` that calculates the length of a given string, and a test function `test_strlen` to check the correctness of the function. The output will be `3` since the input string 'abc' has length 3.