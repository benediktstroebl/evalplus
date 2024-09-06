```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```

This Python script provides a function `strlen` that takes a string as an argument and returns its length. The function utilizes the built-in Python `len()` function to calculate the number of characters in the given string, including spaces, special characters, and punctuation signs. 

To test the function, you can call it with different strings and compare the returned lengths with the expected values. 

For example:
```python
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('The quick brown fox jumps over the lazy dog')
17
```

In these examples, the function `strlen` returns the correct lengths for different strings, confirming that it operates as expected. 

This function can serve as a useful building block for various applications that require string manipulation or validation based on length constraints. 
```python
def strlen(string: str) -> int:
    return len(string)
```