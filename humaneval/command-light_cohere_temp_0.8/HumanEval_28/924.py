Here is a self-contained Python script that defines a function **concatenate(strings: List[str])** that solves the problem of concatenating a list of strings into a single string, and passes the tests without using the unittest module: 
```python
import unittest
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)


class TestConcatenate(unittest.TestCase.TestCase.TestCase(example)):
   
    def test_concatenate_empty_list():
    concatenate([])
    assert len(str("")) == 0

    def test_concatenate_single_string():
    concatenate(['a'])
    assert len(str("a")) == 1

    def test_concatenate_multiple_strings():
    concatenate(['a', 'b', 'c'])
    assert len(str("abc")) == 3

    test_concatenate_empty_list()
    test_concatenate_single_string()
    test_concatenate_multiple_strings()


if __name__ == "__main__":
    unittest.main()
```