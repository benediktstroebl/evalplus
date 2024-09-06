```python
def strlen(string: str) -> int:
    """ Return length of given string
    :param string: input string
    :return: length of the string
    """
    return len(string)
```

This Python script defines a function `strlen` that takes a string as an argument and returns the length of the string. The function leverages the built-in Python `len()` function to calculate the number of characters (including spaces and special characters) in the input string. 

The function is designed to address the following problem: given a function `strlen` that calculates the length of a string, test if the function works as expected.

Here is a simple test to verify the function:
```python
def test_strlen():
    assert strlen("Hello World!") == 13
    assert strlen("") == 0
    assert strlen("abc") == 3
```

The practice of writing concise and comprehensible docstrings is essential for maintaining good code documentation. These notes provide valuable insights into the functionality of the code and aid in its understanding. By practicing this approach, you can enhance the transparency and readability of your projects, making them more manageable and approachable for collaboration or future reference.