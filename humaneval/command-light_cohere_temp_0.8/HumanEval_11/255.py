Here's the self-contained Python script with a function that performs the string XOR operation:
```python
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones.
    >>> str_xor('010', '110')
    '100'
    """
    return ''.join(''.join([x ^ b for, False])
```
This script defines a function called `string_xor`, which takes two strings as input and performs the XOR operation between them. The output is also the result of the operation.

You can use this function to solve the problem and test it using the provided markdown code block.