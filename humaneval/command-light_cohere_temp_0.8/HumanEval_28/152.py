```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :param strings: List of strings to concatenate
    :return: Concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate(['a', 'b', 'c']) == 'abc', "Error in concatenate function"
if __name__ == "__main__":
    test_concatenate()
``` 
This Python code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The function uses the string concatenation technique to combine the supplied list of strings into a single string.