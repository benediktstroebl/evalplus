```python
def flip_case(string):
    return ''.join_case(string)

def test_flip_case():
    assert flip_case('hello') == 'HELLO'
    assert flip_case('world') == 'orld'
    assert flip_case('First') == 'irst'
    assert flip_case('archer') == 'hacker'
``` 
This code defines a function flip_case that takes a string as input and returns a new string where all characters are case-flipped. It uses the final, the `_to_uppercase` function to flip the case of each character in the original string.