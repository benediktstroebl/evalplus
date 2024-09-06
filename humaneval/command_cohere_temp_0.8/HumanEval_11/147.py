```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary `XOR` on two strings consisting of only `0`s and `1`s. The function takes two strings `a` and `b` as inputs and returns their binary `XOR` as a string. This is achieved by using `zip` to iterate over the corresponding bits of both strings, performing `XOR`, and converting the result to a character using `chr`.

Here is an example of how you can use this function to test its functionality:
```python
# Test the string_xor function
assert string_xor('010', '110') == '100'
assert string_xor('110', '010') == '100'
assert string_xor('101', '111') == '000'
``` 

This would return the corresponding binary `XOR` of the two strings. 

We use the `assert` statement to test the function for correctness. The `assert` statement takes two arguments: the left-hand side (LHS) and the right-hand side (RHS). When the LHS is true, Python doesn't raise an exception, and our test passes. If the LHS is false, Python throws an `AssertionError`, indicating that something unexpected happened. This is a fundamental technique in unit testing to check if our code behaves as expected.