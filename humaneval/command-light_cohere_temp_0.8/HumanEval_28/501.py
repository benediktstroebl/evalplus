Here is a self-contained Python script that solves the problem of concatenating lists of strings:
```python
def concatenate(strings: List[str]) -> str:
    return "".join(strings)

def test_concatenate():
    assert concatenate([]) == "", "Should get the empty string"
    assert concatenate(['a']) == "a", "Should get the first string"
    assert concatenate(['a', 'b', 'c']) == "abc", "Should get the concatenated string"
```
The `concatenate` function takes a list of strings and returns the concatenated string, by using the `join()` function to unpack the strings and join them with a space. The `test_concatenate` function tests the `concatenate` function by passing various strings to it and asserting that the output is correct.