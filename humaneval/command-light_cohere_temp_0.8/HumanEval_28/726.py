```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return ''.join(strings)

# Tests
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'

if __name__ == "__main__":
    test_concatenate()
```
This script defines a function **concatenate** that takes a list of strings as input and returns the concatenated string. The function utilizes a string formatting to create the concatenated result. The test_concatenate function verifies the correctness of the **concatenate** function by passing different test cases.