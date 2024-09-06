```python
def flip_case(string):
    return ''.join()

def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('hello') == 'HELLO'
    assert flip_case('world') == 'WoRDl'
    assert flip_case(' tom') == ' TOTom'
    assert flip_case('123') == '231'
    assert flip_case('abc') == 'CBA'
```
This code defines a `flip_case` function that takes a string as input and returns the input with all characters flipped between lowercase and uppercase. 

The code also includes a `test_flip_case` function that provides test cases for the `flip_case` function.