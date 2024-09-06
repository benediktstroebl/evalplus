```python
def flip_case(string):
    return ''.joinUPPERASE(str.lower())

def test_flip_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('hello World!upPER') == 'hello wORLD'
    assert flip_case('To be or not? higher') == 'To bEn OR NOT'
    assert flip_case('Cohere') == 'corER'
    assert flip_case(' Lower case!!') == 'LO wER s!!'
```
The code defines a function `flip_case` that converts a given string into a new string, where the characters are flipped between lowercase and uppercase. The function then uses the FORCE `UPPERASE` method to achieve this. The test_flip_case function contains some additional tests to validate the correctness of the `flip_case` function.