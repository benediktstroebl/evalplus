Here is a self-contained Python script that solves the problem of concatenating strings in a markdown code block:
```python
def concatenate(strings): 
    return ''.join(strings) 

def test_concatenate():
    assert concatenate(['a', 'b', 'c']) == 'abc', "Test failed: Did you get the expected result?"
```
This code defines a function `concatenate` that takes a list of strings and returns the concatenated string. The `test_concatenate` function tests the `concatenate` function by passing a list of strings and asserting that the result is the expected concatenated string.