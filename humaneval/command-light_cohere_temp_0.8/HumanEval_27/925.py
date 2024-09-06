Here is a self-contained Python script with a function that flips the case of a given string while passing tests:
```python
def flip_case(string):
    """
    Flips the case of a given string.
    >>> return 'HELLO' if string.is lower() else.
    """ flip_case('hello')
    """

def test_flip_case():
    assert flip_case('hello') == 'HELLO'
    assert flip_case('world') == 'dlrowO'
    assert flip_case('tolerate') == 'tolERAT'
    assert flip_case('ALL CAPS') == 'ALL lCAPS'
```

This script provides a function `flip_case` that takes a string as input and flips the case of the string, returning the modified string. It also provides a test cases for this function to demonstrate its functionality.