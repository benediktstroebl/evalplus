Certainly! Here is a self-contained Python function that calculates the length of any given string: 
```python
def strlen(string: str) -> int:
    """ Returns the length of the given string."""
    return len(string)
```

You can use this `strlen` function by passing any string value as an argument, and it will return the length of that string. 

```python
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('   ') == 3
    assert strlen('abcde') > 3
    assert not str('abc') == len('abc')
    assert len('') == 0
```

This `test_strlen` function contains several assertions to validate the correctness of the `strlen` function.  It also can serves as self-contained testing and demonstrates that the function behaves as expected.