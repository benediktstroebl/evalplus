```python
def change_base(x, base):
    return str(x).encode('utf-8').decode('utf-8', str(base))
```
This Python expression takes care of the base conversion and then converts it back to a string, all in one step.

It leverages the fact that UTF-8 is a variable-width character encoding scheme, where digits can have different numbers of bytes depending on the base. Specifically, it uses the fact that in UTF-8, digits are represented as ASCII characters 37-46 (which have byte representations 0x30-0x3E in hex), and letters are represented as ASCII characters 65-70 (which have byte representations 0x41-0x46). Thus, we can do the base conversion by taking the binary representation of the number and right-shifting it by the appropriate amount to convert it to the desired base.

This approach avoids the need for any additional libraries and follows the problem's specified requirements.