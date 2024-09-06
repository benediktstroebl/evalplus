Here is a Python script with a self-contained function that solves the problem of XORing two strings in a Markdown code block: 

```python
import typing
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, a and b, consisting only of single characters
    """
    return a ^ b

#Test case 1:
print(string_xor('010', '110'))  
#Expected output: 100

#Test case 2:
print(string_xor('abc', 'abc'))  
#Expected output: 'abc'

#Test case 3:
print(string_xor(''abc', 'abc'))  
#Expected output: 'abc'

#Test case 4:
print(string_xor('', 'abc'))   
#Expected output: 'abc'
```

This Python script defines a function `string_xor` that performs the XOR operation on two input strings, both consisting of only single characters. The function returns the the result of the XOR operation, which is also a string containing only single characters. 

The test cases provided then demonstrate the functionality of the `string_xor` function by passing different strings and expected outputs.