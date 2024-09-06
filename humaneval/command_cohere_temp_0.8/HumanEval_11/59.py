```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
```

This Python script defines a function called `string_xor` that performs binary `XOR` on two input strings `a` and `b`. The function takes two strings as arguments and returns their binary `XOR` as a string. This is achieved by iterating through the characters of both strings, converting them to integers, and performing the `XOR` operation on them. The resulting character, obtained by converting the `XOR` operation's result back to a string, is then added to the `result` string parser.

Here's an example usage of the function:
```python
>>> string_xor('010', '110')
'100'
```
This will return the result '100' which is the binary `XOR` of the two input strings. 

This function can be used to perform binary `XOR` on any two strings consisting only of binary digits '0' and '1'. 

It's important to ensure that both input strings are of equal length to ensure proper XOR operation and output. If the inputs are not of the same length, you can consider padding them with spaces or adding a check to handle the situation differently.