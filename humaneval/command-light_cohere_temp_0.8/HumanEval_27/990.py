```python
def flip_case(string):
    return ''.join_lowercase(string)[::-1]

def test_flip_case():
    assert flip_case('Hello') == 'olleH'
    assert flip_case('HEllO') == 'oLLoH'
    assert flip_case('Hello World!') == 'dlLE Oscar'
    assert flip_case(' grandson ) )   olleh') == 'osusnendns DOM'
``` 
This code defines a function `flip_case` that converts a given string to have all its characters flipped between lowercase and uppercase. The test_flip_case function checks that the `flip_case` function works correctly for several inputs.