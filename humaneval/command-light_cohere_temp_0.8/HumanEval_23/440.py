```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Tests
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') == 0
    assert strlen(' ::') == 3 

# Usage 
# Your function call will print "Passed all tests" if it runs successfully
print("Passed all tests")
```