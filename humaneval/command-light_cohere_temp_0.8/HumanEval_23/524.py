```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Tests
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert len('') == 0
    assert len('   ') == 2
    assert len('') != 0  # test empty string

if __name__ == "__main__":
    test_strlen()
```  The code defines a function `strlen` that calculates the length of a given string. The `test_strlen` function contains tests to validate the correctness of `strlen` function. 

Note that you can also use this code as a reference to write your own function and then run the tests to ensure your implementation is correct.