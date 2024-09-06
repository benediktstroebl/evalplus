```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else lower() else c.isupper() if c.isupper() is (c) else c.isupper()('c'))
   
    """

def test_flipcase():
    assert flip_case('hello') == 'olleH'
    assert flip_case('world') == 'udlrOW'
    assert flip_case('123REALAS') == 'szetsReAlAS'
    assert flip_case(' bowed ') == 'dowBEd '
    assert flip_case('HeLLo.') == 'HeLo '
    assert flip_case(' HEllO  ') == 'LOHO '
    assert flip_case('****OLAlyst') == 'alyostS'

if __name__ == "__main__":
    test_flipcase()
``` 
This script defines a function `flip_case` that converts a given string to have its characters flipped between uppercase and lowercase. The function uses the Python's built-in string method ``.lower() and ``.upper() to accomplish this. 

The function is then tested using the `test_flipcase` function, which contains several assertions that verify the correctness of the `flip_case` function.