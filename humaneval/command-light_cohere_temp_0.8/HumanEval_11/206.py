Here's a self-contained Python function that performs the XOR operation on two strings consisting only of ones:
```python
def string_xor(a: str, b: str) -> str:
    """Perform XOR operation on two strings consisting only of ones.
    >>> str_xor('00101010', '010101010') 
    '1010101010'
    """
    #Convert the input strings to list of ones only
    a = '0' + a if isinstance(a, str) else ['0']
    b = '0' + b if isinstance(b, str) else ['0']
    return ''.join([x ^ y for x in a for y in b])
```
Do you require any further assistance with your Python programming tasks?