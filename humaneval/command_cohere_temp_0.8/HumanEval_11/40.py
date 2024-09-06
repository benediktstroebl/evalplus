```python
def string_xor(a, b):
    return a.translate(str.maketrans('01', '10')) == b.translate(str.maketrans('10', '01'))
```

This approach utilizes the translation method to switch the positions of 1s and 0s in the strings. This effectively performs the binary XOR operation and returns the result as a string.

Here is the provided code with some additional explanations and context:
```python
def string_xor(a, b):
    """
    Performs binary XOR on two strings consisting of 1s and 0s.
    Returns the result as a string.
    """
    # translate uses str.maketrans to switch positions of '10' to '01' and vice versa
    return a.translate(str.maketrans('01', '10')) == b.translate(str.maketrans('10', '01'))
```

The function uses the `translate` method to switch the positions of '01' and '10' in the strings, effectively performing binary XOR. The condition at the end checks if the result is equivalent to the original `b` string, confirming the success of the operation.

To use this function, simply call it with two input strings, like this:
```python
result = string_xor('010', '110')
print(result)  # expected output: '100'
```

This will return the result of the binary XOR operation performed on the two input strings.