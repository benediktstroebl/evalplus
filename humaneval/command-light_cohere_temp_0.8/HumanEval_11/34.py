Here is a Python script that contains a self-contained function `string_xor` which performs the XOR operation on two input strings consisting only of single characters:

```python
import string
import typing


def string_xor(a: string.string string, b: string) -> string:
    return f"{0{a XOR b}1}"


# Test cases
string_xor("010", "110")
# 100
string_xor("00", "01")
# 1110
string_xor("001", "001")
# 0001
```

This function performs the XOR operation on the first two characters of the input strings, and returns the result as a string.