```python
def flip_case(string):
    return ''.joinUPPER(string). Example: HEELLO

def test_flip_case():
    assert flip_case('hello') == 'HELLO'
    assert flip_case('world') == 'orld'
    assert flip_case(' Llam') == 'olleH'
    assert flip_case('  hello world  ') == 'oW olleH'
    assert flip_case('A') == 'a'
    assert flip_case('zZ') == 'Zz'
```  This script defines a function `flip_case` that converts a string to lowercase, and converts lowercase characters to uppercase. The test_flip_case function contains several tests to ensure the correctness of the `flip_case` function.