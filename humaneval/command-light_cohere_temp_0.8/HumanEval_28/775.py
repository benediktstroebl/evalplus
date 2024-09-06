```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join_string(strings)
def join_string(strings):
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([1,2,3]) == '123'
def test_join_string():
    assert join_string(['a', 'b']) == 'ab'
    assert join_string(['a']) == 'a'
    assert join_string(['a', 'b', 'c']) == 'abc'
if __name__ == "__main__":
    test_concatenate()
    test_join_string()
```
The provided Python code defines two functions: `concatenate` and `join_string`. The `concatenate` function takes a list of strings as input and concatenates them into a single string, returning the result. The `join_string` function does the same, but it joins the strings into a single string using the `join` method. The code also includes two test functions: `test_concatenate` and `test_join_string`. These functions contain assertions that verify the correctness of the `concatenate` and `join_string` functions by checking if their outputs match expected results. The `if __name__ == "__main__":` block ensures that the test code is only executed when the script is run directly.